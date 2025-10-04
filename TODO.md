TEST -- using AGENTS.md file
# TODO
✅ [p1] Remove the obsolete MWE viewer by deleting dev/test_objects/mwe_viewer.html and stripping all navigation links or tests that reference it.
✅ [p1] Excise the broken orbit viewer references from marketing copy and persistence keys so only the 2D survey and FPV flows remain.
✅ [p1] Persist placed GLTF assets across the 2D survey and FPV views by serializing placements to shared storage and restoring them when either view loads.
✅ [p1] Draft two prototype approaches for connecting items with curved joints, including how to register connection points on bounding boxes.
Prototypes should target draggable Bézier splines and, if feasible, a physics-based cable simulation. Cables must connect by clicking endpoints and allow realistic movement with a max length limit (e.g., 10 ft / 3 m). Physics-based routing may bias cables to avoid objects, but manual bend points remain acceptable. Some machines can hold cables in service loops, so only max length is enforced.
✅ [p1] Identify required metadata schema updates so cables can snap to defined connection sockets on each asset. No rotation/orientation data is required. Metadata should only define which cable types are valid for which machine types. The goal is simple layout validation, not CAD-level detail.
✅ [p1] Stand up a shared cable catalog describing cable types, asset socket anchors, and default max lengths so both survey and FPV modes can reference identical metadata.
✅ [p1] Extend the layout store, persistence helpers, and normalization logic to include a cables array with endpoints, control points, and cached length/status data.
✅ [p1] Implement 2D survey affordances for sockets (hover highlights) and Bézier cable drawing/editing, including snapping control handles and persistence of bend points.
✅ [p1] Render cable paths in the FPV demo via Three.js lines/tubes, reusing layout cables and mirroring color coding for cable types.
✅ [p1] Add focused regression coverage asserting cable metadata availability and layout serialization fields so future refactors keep the feature intact.
✅ [p2] Diagnose why cables fail to render in FPV view and update the Three.js scene graph so saved cables become visible.
✅ [p2] Add a wall-mounted gas socket asset with metadata (type tags, cable compatibility, thumbnail) and expose it in the catalog.
✅ [p2] Introduce a wall feedthrough asset that provides paired connection sockets on both sides of a wall and persists placement metadata.
✅ [p2] Expose connection anchors on bulky equipment meshes so users can attach cables/lines without mesh occlusion (adjust anchor offsets or hit areas).
 🔲 [p2] Extend regression tests to cover importing a saved layout and switching between tabs without losing state.
🔲 [p2] Add an automated check that first-person mode stops moving when no input is pressed.
🔲 [p2] Backfill regression coverage for the new FPS module loader path or document why automated coverage is deferred.
🔲 [p2] Adjust the wall-door overlap so the door remains visible when placed (either by carving a doorway gap or thickening the door asset). If possible, implement dynamic wall subtraction that updates when the door is moved. Otherwise, fallback to thickened door assets.
🔲 [p2] Reposition or resize the wall socket asset so it is visible in the wall view; confirm desired thickness. Thicker socket meshes are acceptable. Sockets can protrude slightly since real sites vary (flush vs mounted tubes). Primary purpose is indicating utility placement for survey consistency.
🔲 [p2] Define new catalog entries for chiller, N2 bottle, wall air line barb, bottled air line, and resizable tables, including required metadata (dimensions, connection points, thumbnails).
✅ [p1] Implement color-coded cable/line variants for power (black), air (white), N2 (green), ground (green/yellow stripe), vacuum (transparent white), water (blue), and Ethernet (yellow) lines. These should appear in both 2D and FPV views as real placed objects. Goal is realistic layout checking and annotating facility responsibilities when line lengths exceed provided equipment.
🔲 [p3] Catalog reusable "glass light" theme tokens for other room survey prototypes and expand the shared theme library as new looks emerge.
🔲 [p3] Evaluate additional camera input affordances (e.g., touch gestures and keyboard shortcuts) for the 3D first-person demo after the next round of feedback.
🔲 [p3] Gate the FPS "Enter Walk Mode" button when pointer lock is unsupported and surface a toast to clarify the disabled state.
🔲 [p3] Rename all UI copy and persistence keys from "FPS" to "FPV" across the site.
🔲 [p3] Double the forward/backward walk speed in FPV mode so perspective traversal feels faster.
🔲 [p3] Raise the FPV camera height (and related collision bounds) to approximate human eye level rather than dog-height perspective.
🔲 [p4] Add optional keybindings (e.g., Z/C) to rotate selected objects around the X axis while retaining Q/E for Z-axis rotation. Rotation can snap to increments. Smooth analog control is not required—CAD tools handle high-fidelity adjustments later.
🔲 [p4] Export format is in such a way that OpenSCAD or FreeCAD may be able to render the finalized room.  
Evaluate feasibility of exporting layouts in a format that these CAD tools can interpret for further refinement.
