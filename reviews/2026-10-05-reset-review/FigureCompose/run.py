"""Local file tools for the Codex-led figure workflow; no model orchestration."""
import argparse
import collections
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
PVA = ROOT / 'papervizagent'
AFE = ROOT / 'AutoFigure-Edit'
BANK = PVA / 'data/PaperBananaBench/diagram'


def save_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding='utf8') != text:
        raise RuntimeError(f'Existing artifact differs: {path}. Use a new --out directory.')
    path.write_text(text, encoding='utf8')


def references():
    rows = json.loads((BANK / 'ref.json').read_text(encoding='utf8'))
    for row in rows:
        row['path_to_gt_image'] = str((BANK / row['path_to_gt_image']).resolve())
        if not Path(row['path_to_gt_image']).is_file():
            raise RuntimeError('Missing reference image: ' + row['path_to_gt_image'])
    return rows


def prepare(args):
    brief = args.request_file.read_text(encoding='utf8') if args.request_file else args.request
    if not brief:
        raise RuntimeError('Supply a natural-language --request or --request-file.')
    out = args.out.resolve()
    rows = references()
    selected = [row for row in rows if row['id'] in args.reference]
    if set(args.reference) - {row['id'] for row in selected}:
        raise RuntimeError('Unknown reference ID in Codex selection.')
    if len(selected) > 3:
        raise RuntimeError('The minimal experiment uses at most three references.')
    save_text(out / 'request.txt', brief)
    if args.context:
        save_text(out / 'context.md', args.context.read_text(encoding='utf8'))
    save_text(out / 'reference-candidates.json', json.dumps(rows, ensure_ascii=False, indent=2))
    if selected:
        save_text(out / 'selected-references.json', json.dumps(selected, ensure_ascii=False, indent=2))
    save_text(out / 'reference-sources.json', (BANK / 'reference_sources.json').read_text(encoding='utf8'))
    print(f'Prepared input and {len(rows)} references: {out}')
    print('Codex selects references, inspects images, writes the prompt, calls the built-in image tool, and reviews its PNG. This command does not generate an image.')


def check_svg(path):
    root = ET.parse(path).getroot()
    if root.tag.rsplit('}', 1)[-1] != 'svg':
        raise RuntimeError('Document root is not SVG.')
    counts = collections.Counter(e.tag.rsplit('}', 1)[-1] for e in root.iter())
    texts = [''.join(e.itertext()).strip() for e in root.iter() if e.tag.rsplit('}', 1)[-1] == 'text']
    vectors = sum(counts[tag] for tag in ('path', 'rect', 'line', 'polyline', 'polygon', 'circle', 'ellipse'))
    if not any(texts) or not vectors:
        raise RuntimeError('SVG needs editable text and vector shapes; raster wrapping does not pass.')
    viewbox = root.get('viewBox', '').replace(',', ' ').split()
    width, height = (float(viewbox[2]), float(viewbox[3])) if len(viewbox) == 4 else (float(root.get('width', '0').removesuffix('px')), float(root.get('height', '0').removesuffix('px')))
    for e in root.iter():
        if e.tag.rsplit('}', 1)[-1] != 'image':
            continue
        def extent(name, total):
            value = e.get(name, '0')
            return total * float(value[:-1]) / 100 if value.endswith('%') else float(value.removesuffix('px'))
        if width and height and extent('width', width) >= .85 * width and extent('height', height) >= .85 * height:
            raise RuntimeError('Near-full-canvas raster embedded; editable reconstruction fails.')
    return {'element_counts': dict(counts), 'text': texts, 'vector_count': vectors,
            'note': 'Structural check only. Accuracy, raster coverage and visual fidelity require image review.'}


def afe_module():
    sys.path.insert(0, str(AFE))
    import autofigure2
    return autofigure2


def import_raster(args):
    if not args.raster or not args.raster.is_file():
        raise RuntimeError('Supply the actual generated image with --raster.')
    target = args.out.resolve() / 'figure.png'
    if target.exists():
        raise RuntimeError(f'Image already exists: {target}. Use a new --out directory.')
    from PIL import Image
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(args.raster) as image:
        image.save(target, format='PNG')
    print('Imported actual generated raster:', target)


def reconstruct(args):
    raster = args.raster.resolve() if args.raster else args.out.resolve() / 'figure.png'
    if not raster.is_file():
        raise RuntimeError('No actual raster exists; complete Codex image generation first.')
    keys = {'gemini': 'GOOGLE_API_KEY', 'openai_response': 'OPENAI_API_KEY',
            'openrouter': 'OPENROUTER_API_KEY', 'bianxie': 'BIANXIE_API_KEY', 'custom': 'AUTOFIGURE_API_KEY'}
    missing = []
    key = os.getenv(keys[args.svg_provider])
    if not key:
        missing.append(f'{args.svg_provider} SVG model service is unconfigured')
    if args.sam_backend == 'roboflow' and not (os.getenv('ROBOFLOW_API_KEY') or os.getenv('API_KEY')):
        missing.append('SAM3 Roboflow service is unconfigured')
    if args.sam_backend == 'fal' and not os.getenv('FAL_KEY'):
        missing.append('SAM3 fal service is unconfigured')
    if args.sam_backend == 'local' and importlib.util.find_spec('sam3') is None:
        missing.append('local SAM3 package is unavailable')
    if missing:
        raise RuntimeError('Full AutoFigure-Edit reconstruction unavailable: ' + '; '.join(missing) + '. Stage 1 remains usable. No credential configuration was attempted.')
    editable = args.out.resolve() / 'editable'
    if editable.exists():
        raise RuntimeError('Existing editable directory; use a new --out directory.')
    result = afe_module().method_to_svg(input_figure_path=str(raster), output_dir=str(editable),
        provider=args.svg_provider, api_key=key, base_url=args.svg_base_url,
        svg_gen_model=args.svg_model, sam_backend=args.sam_backend,
        rmbg_model_path=str(args.rmbg_model_path) if args.rmbg_model_path else None,
        optimize_iterations=args.svg_iterations, enable_upscale=False)
    final = Path(result['final_svg_path'])
    save_text(editable / 'structure-check.json', json.dumps(check_svg(final), ensure_ascii=False, indent=2))
    print('Upstream reconstructed SVG:', final)


def render_svg(source, target):
    """Call an installed SVG renderer; no custom rendering implementation."""
    import cairosvg
    cairosvg.svg2png(url=str(source), write_to=str(target))


def edit_probe(source, out):
    """Edit copies of one visible label and shape and check actual rerenders."""
    from PIL import Image, ImageChops
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
    baseline = Image.open(out / 'svg-preview.png').convert('RGB')
    results = {}
    def visible_elements(element):
        if element.tag.rsplit('}', 1)[-1] in ('defs', 'marker', 'clipPath', 'mask', 'pattern', 'title', 'desc'):
            return
        yield element
        for child in element:
            yield from visible_elements(child)
    folder = out / 'edit-probe'
    folder.mkdir(exist_ok=True)
    for kind in ('text', 'vector'):
        tree = ET.parse(source)
        elements = list(visible_elements(tree.getroot()))
        if kind == 'text':
            element = next((e for e in elements if e.tag.rsplit('}', 1)[-1] == 'text' and (e.text or '').strip()), None)
            if element is None:
                raise RuntimeError('No visible text for edit probe.')
            old = element.text
            element.text = 'EDIT PROBE'
            change = {'original': old, 'edited': 'EDIT PROBE'}
        else:
            element = next((e for e in elements if e.tag.rsplit('}', 1)[-1] in ('rect', 'path', 'circle', 'polygon') and e.get('fill') not in (None, 'none', 'white', '#fff', '#ffffff') and e.get('width') != tree.getroot().get('width')), None)
            if element is None:
                raise RuntimeError('No colored vector shape for edit probe.')
            old = element.get('fill')
            element.set('style', (element.get('style', '') + ';fill:#e93673').lstrip(';'))
            change = {'original_fill': old, 'edited_fill': '#e93673'}
        svg_path = folder / f'{kind}.svg'
        png_path = folder / f'{kind}.png'
        tree.write(svg_path, encoding='utf-8', xml_declaration=True)
        render_svg(svg_path, png_path)
        with Image.open(png_path) as image:
            difference = ImageChops.difference(baseline, image.convert('RGB')).getbbox()
        if not difference:
            raise RuntimeError(f'{kind} edit did not change the rendered image.')
        results[kind] = {'passed': True, 'change': change, 'difference_bbox': difference,
                         'svg': str(svg_path), 'png': str(png_path)}
    return results


def finalize_template(args):
    # Codex authors the SVG; this utility saves/checks/renders it without model calls.
    if not args.template or not args.template.is_file():
        raise RuntimeError('Supply the Codex-authored reconstruction with --template.')
    inputs = (args.inputs or args.out).resolve()
    required = ['figure.png', 'request.txt', 'generation-prompt.txt', 'selected-references.json']
    missing = [name for name in required if not (inputs / name).is_file()]
    if missing:
        raise RuntimeError('Stage 2 inputs missing: ' + ', '.join(missing))
    json.loads((inputs / 'selected-references.json').read_text(encoding='utf8'))
    source = args.template.read_text(encoding='utf8')
    ET.fromstring(source)
    out = args.out.resolve()
    if any((out / name).exists() for name in ('figure.svg', 'svg-preview.png', 'editability-check.json')):
        raise RuntimeError('Stage 2 outputs already exist; use a new --out and retain --inputs.')
    save_text(out / 'template.svg', source)
    if args.icon_crops:
        # Crops are explicitly Codex-selected regions, not fabricated SAM detections.
        crops = json.loads(args.icon_crops.read_text(encoding='utf8'))
        afe_module().replace_icons_in_svg(str(out / 'template.svg'), crops, str(out / 'figure.svg'))
    else:
        save_text(out / 'figure.svg', source)
    report = check_svg(out / 'figure.svg')
    render_svg(out / 'figure.svg', out / 'svg-preview.png')
    report['edit_probe'] = edit_probe(out / 'figure.svg', out)
    report['inputs'] = {name: str(inputs / name) for name in required}
    report['inputs']['context.md'] = str(inputs / 'context.md') if (inputs / 'context.md').is_file() else None
    report['provenance'] = 'Codex-authored reconstruction; stdlib XML and installed CairoSVG/Pillow. AutoFigure-Edit optional only for explicit icon assembly/full API stage.'
    report['scientific_review'] = 'pending Codex review of actual output'
    report['visual_review'] = 'pending Codex review of actual preview'
    report['native_editor_test'] = 'not performed'
    save_text(out / 'editability-check.json', json.dumps(report, ensure_ascii=False, indent=2))
    print('Saved figure.svg, svg-preview.png, editability-check.json:', out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--request')
    group.add_argument('--request-file', type=Path)
    parser.add_argument('--context', type=Path)
    parser.add_argument('--stage', choices=['prepare', 'references', 'raster', 'svg', 'finalize', 'check'], default='prepare')
    parser.add_argument('--out', type=Path, default=ROOT / 'outputs/codex-pi0')
    parser.add_argument('--reference', action='append', default=[], help='Internal Codex selection; users need not choose IDs.')
    parser.add_argument('--query', help='Literal metadata filter, not automatic semantic ranking.')
    parser.add_argument('--raster', type=Path)
    parser.add_argument('--template', type=Path)
    parser.add_argument('--icon-crops', type=Path, help='Internal Codex crop records for local upstream icon assembly; not SAM output.')
    parser.add_argument('--inputs', type=Path, help='Stage 2 input folder when saving a separate reconstruction revision.')
    parser.add_argument('--svg-provider', choices=['gemini', 'openai_response', 'openrouter', 'bianxie', 'custom'], default='openai_response')
    parser.add_argument('--svg-model')
    parser.add_argument('--svg-base-url')
    parser.add_argument('--sam-backend', choices=['local', 'roboflow', 'fal'], default='roboflow')
    parser.add_argument('--rmbg-model-path', type=Path)
    parser.add_argument('--svg-iterations', type=int, default=0)
    args = parser.parse_args()
    needs_environment = args.stage == 'svg' or (args.stage == 'raster' and importlib.util.find_spec('PIL') is None) or (args.stage == 'finalize' and (importlib.util.find_spec('cairosvg') is None or args.icon_crops))
    if needs_environment:
        python = AFE / '.venv' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
        if Path(sys.executable).resolve() != python.resolve():
            subprocess.run([str(python), '-X', 'utf8', str(ROOT / 'run.py'), *sys.argv[1:]], cwd=ROOT, check=True)
            return
    if args.stage == 'references':
        rows = references()
        if args.query:
            rows = [r for r in rows if args.query.casefold() in (str(r['content']) + str(r['visual_intent'])).casefold()]
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    elif args.stage == 'prepare':
        prepare(args)
    elif args.stage == 'raster':
        import_raster(args)
    elif args.stage == 'svg':
        reconstruct(args)
    elif args.stage == 'finalize':
        finalize_template(args)
    else:
        if not args.template:
            parser.error('--stage check requires --template.')
        print(json.dumps(check_svg(args.template), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, OSError, ValueError, ET.ParseError, subprocess.CalledProcessError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
