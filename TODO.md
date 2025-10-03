TEST -- using AGENTS.md file
# TODO
✅ [p1] Remove the obsolete MWE viewer by deleting dev/test_objects/mwe_viewer.html and stripping all navigation links or tests that reference it.
✅ [p1] Excise the broken orbit viewer references from marketing copy and persistence keys so only the 2D survey and FPV flows remain.
✅ [p1] Persist placed GLTF assets across the 2D survey and FPV views by serializing placements to shared storage and restoring them when either view loads.
🔲 [p1] Draft two prototype approaches for connecting items with curved joints, including how to register connection points on bounding boxes. _Need clarification: should prototypes target draggable Bézier splines, physics-based cable simulation, or another approach?_
🔲 [p1] Identify required metadata schema updates so cables can snap to defined connection sockets on each asset. _Need clarification: do sockets require orientation data and capacity limits per asset?_
🔲 [p2] Extend regression tests to cover importing a saved layout and switching between tabs without losing state.
🔲 [p2] Add an automated check that first-person mode stops moving when no input is pressed.
🔲 [p2] Backfill regression coverage for the new FPS module loader path or document why automated coverage is deferred.
🔲 [p2] Adjust the wall-door overlap so the door remains visible when placed (either by carving a doorway gap or thickening the door asset). _Need clarification: should we prioritize boolean wall subtraction or simply increase door thickness?_
🔲 [p2] Reposition or resize the wall socket asset so it is visible in the wall view; confirm desired thickness. _Need clarification: should sockets protrude beyond wall faces, or is a thicker mesh acceptable?_
🔲 [p2] Define new catalog entries for chiller, N2 bottle, wall air line barb, bottled air line, and resizable tables, including required metadata (dimensions, connection points, thumbnails).
🔲 [p2] Implement color-coded cable/line variants for power (black), air (white), N2 (green), ground (green/yellow stripe), vacuum (transparent white), water (blue), and Ethernet (yellow) lines. _Need clarification: should these appear in both 2D and FPV views simultaneously?_
🔲 [p3] Catalog reusable "glass light" theme tokens for other room survey prototypes and expand the shared theme library as new looks emerge.
🔲 [p3] Evaluate additional camera input affordances (e.g., touch gestures and keyboard shortcuts) for the 3D first-person demo after the next round of feedback.
🔲 [p3] Gate the FPS "Enter Walk Mode" button when pointer lock is unsupported and surface a toast to clarify the disabled state.
🔲 [p3] Rename all UI copy and persistence keys from "FPS" to "FPV" across the site.
🔲 [p3] Double the forward/backward walk speed in FPV mode so perspective traversal feels faster.
🔲 [p3] Raise the FPV camera height (and related collision bounds) to approximate human eye level rather than dog-height perspective.
🔲 [p4] Add optional keybindings (e.g., Z/C) to rotate selected objects around the X axis while retaining Q/E for Z-axis rotation. _Need clarification: should rotations snap to increments or allow smooth analog control?_
