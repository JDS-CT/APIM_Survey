TEST -- using AGENTS.md file
# TODO
✅ [p2] Extend regression tests to cover importing a saved layout and switching between orientation tabs without losing state.
  - [x] Capture a layout export fixture containing floor and wall placements plus cables.
  - [x] Write a survey store test that loads the fixture, flips tabs, and asserts selection/cable context persists.
✅ [p2] Improve first-person perspective scale cues and idle behavior.
  - [x] Add a failing FPV test ensuring the default avatar height is ~1.6 m and that 1 m markers render in the scene graph.
  - [x] Implement camera/controller height adjustments and add visual measurement helpers in 3D.
  - [x] Add an automated check that first-person mode stops moving when no input is pressed.
  - [x] Author a unit test around the FPV movement controller that steps the simulation without inputs and asserts zero velocity.
  - [x] Mock pointer lock/input sources so the test runs in headless environments.
✅ [p2] Backfill regression coverage for the new FPV module loader path or document why automated coverage is deferred.
  - [x] Identify loader behaviors lacking tests and create targeted coverage, or log blockers in PROBLEMS.md if testing is infeasible.
✅ [p2] Synchronize the orientation tabs with 2D layout state so switching tabs updates the canvas projection without losing context.
  - [x] Wire tab clicks to the existing orientation setter and ensure canvases re-render with the selected wall/floor/ceiling view.
  - [x] Preserve active selections and cable editing handles when orientation changes.
  - [x] Add regression coverage for the new tab-driven projection changes.
✅ [p2] Implement 2D scale markers so users can quickly gauge distances without counting snap grids.
  - [x] Design a subtle measurement overlay (e.g., rulers or labeled tick marks) that respects the current zoom and snap size.
  - [x] Render the overlay in the survey canvas layer without interfering with item interactions.
  - [x] Add configuration to toggle markers for future customization and cover with a unit or integration test.
✅ [p2] Audit object scale in FPV mode and adjust avatar or scene scaling for accurate human perspective.
  - [x] Verify current unit conversions between survey data and Three.js scene dimensions.
  - [x] Raise the FPV camera height and adjust collision bounds to approximate human eye level.
  - [x] Update default avatar/controller scale factors so furniture and walls feel accurate, adding regression tests where feasible.
✅ [p2] Document and implement visible scale references in 3D review when practical.
  - [x] Investigate lightweight scene helpers (e.g., floor grid decals or meter sticks) and prototype an unobtrusive option.
  - [x] Document the helper and default it on while outlining how to disable or gate it after design feedback.
✅ [p2] Add thermostat assets for wall and ceiling contexts, including metadata, thumbnails, and distinct dangling sensor meshes when placed on ceilings.
  - [x] Produce catalog definitions and 2D/3D representations for each thermostat variant.
  - [x] Ensure placement rules respect wall versus ceiling orientation and cover with tests.
✅ [p2] Define catalog entries for chiller, N2 bottle, wall air line barb, bottled air line, and resizable tables with required metadata.
  - [x] Capture dimensions, socket metadata, thumbnails, and placement defaults for each new item.
  - [x] Add regression coverage for catalog loading and placement serialization.
🔲 [p3] Catalog reusable "glass light" theme tokens for future room survey prototypes.
  - [ ] Extract existing colors/typography/elevation into shared theme primitives.
  - [ ] Publish guidance in the design tokens documentation and cover with snapshot tests if applicable.
🔲 [p3] Evaluate additional camera input affordances (touch gestures, keyboard shortcuts) for the FPV demo after the next feedback round.
  - [ ] Audit current input handling and list candidate enhancements.
  - [ ] Prototype at least one alternative control scheme behind a development flag and document findings.
🔲 [p3] Gate the FPV "Enter Walk Mode" button when pointer lock is unsupported and show a toast explaining the disabled state.
  - [ ] Detect pointer-lock availability on load and during capability changes.
  - [ ] Disable the button with accessible messaging and add coverage for both supported/unsupported cases.
🔲 [p3] Rename all UI copy and persistence keys from "FPS" to "FPV" across the site.
  - [ ] Inventory code, tests, and stored keys that still reference FPS.
  - [ ] Apply renames and update migration helpers/tests to prevent regressions.
🔲 [p3] Double the forward/backward walk speed in FPV mode so traversal feels faster.
  - [ ] Update controller constants and ensure acceleration remains stable.
  - [ ] Refresh FPV movement tests to reflect the new baseline speed.
🔲 [p3] Introduce a translucent "Ghost" survey equipment marker asset representing portable sensor placements.
  - [ ] Design catalog metadata, 2D iconography, and 3D mesh for the ghost sensor marker.
  - [ ] Allow annotations for recorded sensor data and persist placements in exports, with regression tests.
🔲 [p4] Document the CAD export backlog with a concise summary of current state and desired FreeCAD/STEP deliverable.
  - [ ] Capture the JSON interchange today, outline the target CAD package, and specify validation goals in a short paragraph.
  - [ ] Cross-link the summary to implementation tasks so future work is discoverable.
🔲 [p4] Add optional keybindings (e.g., Z/C) to rotate selected objects around the X axis while retaining Q/E for Z-axis rotation.
  - [ ] Implement the bindings with snap increments and guard against conflicts.
  - [ ] Cover new shortcuts with interaction tests.
🔲 [p4] Export layouts in a format that OpenSCAD or FreeCAD can interpret for further refinement.
  - [ ] Evaluate candidate export schemas and outline conversion steps from survey JSON to CAD-friendly outputs.
  - [ ] Implement the chosen export pipeline or document blockers with actionable follow-ups.
