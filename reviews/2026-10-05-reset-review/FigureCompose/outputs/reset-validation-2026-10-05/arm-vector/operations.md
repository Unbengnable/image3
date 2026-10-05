# Measured operations and stopping record

- Initial measured UTC time: 2026-10-05 12:57:54, immediately after required scope/input reading. The preceding brief read was not separately timed.
- Pre-SVG design-decision hash: 65279979FB9FCC5DAA0DF53A6AA1CE47C2844BA736142FA655916C4F264EC462. File last-write time at hashing: 2026-10-05 12:59:05 UTC. The first SVG was created later.
- Initial SVG and render completed by 13:02:46 UTC. Render attempt 1 succeeded; view_image call 1 inspected it shortly afterward.
- 13:03 UTC: first-render criticism saved. The inline Python glyph edit failed at command parsing; it left the copied SVG unchanged. No render was attempted by that failed command.
- Glyph repair through Python stdin and render attempt 2 completed by 13:03:57 UTC. Native tspan markup replaced unsupported Unicode subscript glyphs. The repaired SVG/render are retained. No composition changed.
- Consolidated revision changed retained-position marks and the auxiliary-token route. Render attempt 3 succeeded. View_image call 2 inspected it at 13:04:58 UTC. No further main revision was made.
- Main SVG and PNG were frozen by exact copying at 13:06:17 UTC. The freeze is independent of caption/notes completion. The final preview is the already inspected third render, not a separately rerendered image.
- Separate semantic-edit render attempt 4 succeeded by 13:07:39 UTC; view_image call 3 inspected it immediately afterward. No repair or second revision of this copy was necessary.
- Total successful renders: 4. Failed renders: 0. Image viewing calls: 3. Imagegen calls: 0. External paid API calls: 0. New dependency installations: 0. Syntax/render-only repairs: 1. Consolidated main scientific/visual revisions: 1. Separate semantic edits: 1.

File creation/last-write UTC times, input hashes, output hashes and end time are in provenance.json and cost.json. Filesystem times may differ from inspection time because tools return after completion. Token usage, subscription monetary cost and active thinking time are unavailable. Wall time is elapsed time between measured clock samples and does not establish compute parity with the raster arm.

The author stops after this freeze and copy-edit evidence. Any later reviewer judgment is recorded externally without sending improvement requests back to this author.
