
# Changelog

## 2025-10-04T17:06:49Z
- feat: complete step [p1] Align wall elevation drag interactions with the shared floor snap pipeline so wall tab edits honor snap increments and HUD feedback.
- feat: complete step [p1] Rework default cable sag so untouched splines drop to the floor quickly and track the 2D path via updated control point defaults and markup tests.

## 2025-10-04T15:29:44Z
- feat: complete step [p1] Mirror 2D cable path edits into the FPV scene by ingesting storage updates and rebuilding Three.js tubes from the shared layout.
- fix: complete step [p1] Remove plan-view clamps on cable handles and bend inserts while persisting absolute spline coordinates for out-of-bounds adjustments.
- feat: complete step [p2] Add wall-mounted height controls to the survey UI and honor socket mount offsets when resolving cable anchors.
- feat: complete step [p2] Retune default cable slack so sampled control handles sag toward the floor consistently across 2D and 3D renders.

## 2025-10-06T05:30:00Z
- fix: complete step [p1] Wire orientation tab clicks to update the SVG data attribute so wall and ceiling projections replace the floor plan without losing selection context.
- feat: complete step [p2] Gate the survey scale overlay behind a config flag and documentable tests so rulers render without blocking interactions.
- docs: Refine the design-principles Q&A to emphasize custom notes, follow-up integration, and sensor context.
- test: Extend markup assertions to cover the SVG orientation attribute setter and the FPV human eye-height constant.

## 2025-10-06T00:00:00Z
- feat: complete step [p2] Synchronize the orientation tabs with layout state and add wall elevation rendering so switching tabs updates projections without losing context.
- feat: complete step [p2] Add scale overlays to the 2D survey canvas so users can gauge room dimensions at a glance.
- feat: complete step [p2] Align FPV measurements with survey units, raise the camera to human height, and introduce floor/vertical scale markers for spatial context.
- docs: Capture design principles explaining why the web survey exists alongside FreeCAD reference flows.
- test: Extend markup coverage for the orientation elevation overlays and FPV scale helpers.

## 2025-10-05T12:30:00Z
- feat: complete step [p2] Add tabbed orientation controls above the 2D survey canvas for floor, wall, ceiling, and custom wall views with a View Selected shortcut tied to the existing wall selector.
- test: extend frontend markup coverage to assert the new orientation tab controls render with floor, ceiling, and wall targets.

## 2025-10-05T08:15:00Z
- fix: complete step [p1] Restore the cable type dropdown by restructuring the shared default catalog so fallback metadata loads before the fetch completes.
- feat: complete step [p1] Seed the default survey and FPV layouts with a sample microscope power cable for instant visualization and persistence regression coverage.
- fix: complete step [p2] Thicken FPV door meshes and offset them from the wall plane to eliminate z-fighting while keeping both sides visible.
- feat: complete step [p2] Render wall sockets and feedthroughs in FPV using catalog-derived dimensions, colors, and depth offsets so ports appear in the 3D view.
- chore: complete step [p3] Switch the sample asset loader to a single-file GLB and drop the multi-file GLTF bundle for simpler asset distribution.
## 2025-10-05T04:30:00Z
- fix: complete step [p2] Restore FPV cable rendering by defining shared sample density constants and honoring wall socket offset directions.
- feat: complete step [p2] Add catalog metadata and UI affordances for wall-mounted gas sockets and dual-sided feedthroughs across survey and FPV views.
- fix: complete step [p2] Surface wall connection anchors above equipment meshes so sockets remain clickable when placing cables.
- test: extend frontend markup coverage for the new wall item options and FPV cable sampling guard.

## 2025-10-05T00:00:00Z
- feat: complete step [p1] Ship a shared cable catalog default script and fallbacks so cable type dropdowns populate even when the external JSON fails to load.
- feat: complete step [p1] Teach both survey and FPV views to reuse the shared defaults for color-coded cable rendering across power, air, N2, ground, vacuum, water, and Ethernet lines.
- test: extend frontend markup coverage to assert the shared cable defaults are referenced by both experiences.

## 2025-10-03T21:50:07Z
- feat: Implemented cable bend insertion/removal and draggable bend handles in the 2D survey so multi-segment Bézier routes can be authored.
- feat: Taught the FPV demo to honor persisted bend points by sampling chained cubic segments when generating tube geometry and lengths.
- test: Added frontend markup assertions covering the new cable bend controls and handler functions.

## 2025-10-03T21:39:02Z
- feat: Stand up a shared cable catalog and extend layout persistence so cables serialize with endpoints, bend points, and status.
- feat: Add 2D survey socket overlays with Bézier cable creation, draggable handles, and length validation UI.
- feat: Render FPV cable tubes in Three.js using shared metadata and update statuses after layout changes.
- test: Extend frontend markup coverage to assert cable catalog wiring and layout snapshot fields for cables.

## 2025-10-03T18:57:17Z
- docs: complete step [p1] Document curved cable connection prototypes covering Bézier and physics-driven approaches with bounding-box socket registration.
- docs: complete step [p1] Outline cable metadata schema updates so sockets declare allowed cable types for validation across survey and FPV views.

## 2025-10-03T16:31:24Z
- chore: complete step [p1] Remove the obsolete MWE viewer, its archived assets, and navigation hooks so the prototype only links to supported flows.
- chore: complete step [p1] Excise orbit viewer references from the landing page, docs, and persistence keys to align messaging with the FPV workflow.
- feat: complete step [p1] Sync GLTF asset placement across the 2D survey and FPV by sharing a layout storage key and serializing asset transforms.
- test: extend frontend markup checks to cover the shared layout key, GLTF asset persistence helpers, and absence of the legacy tabs.

## 2025-10-03T13:58:00Z
- fix: complete step [p1] Harden the FPS GLTF loader with bounding-box diagnostics, scale heuristics, and UI status updates so invisible imports surface actionable feedback.
- feat: complete step [p1] Auto-scale and frame loaded GLTF assets while adding a reset control that recenters the camera on demand for recovery.
- test: complete step [p1] Extend frontend markup assertions to cover the asset status UI, reset control, and loader messaging hooks.

## 2025-10-03T12:34:00Z
- fix: complete step [p1] Clamp the pointer-lock walk velocity to zero when no movement keys are held so the orbit and MWE viewers no longer drift while idle.
- feat: complete step [p1] Restore a translation snap slider in the FPS demo that drives both TransformControls and Hand Mode nudges.
- test: complete step [p1] Extend the frontend markup assertions to cover the snap slider hooks and the new idle-movement guard.

## 2025-10-03T11:26:46Z
- fix: complete step [p1] Investigate and resolve the First-Person Demo controls mismatch by trapping Space/Shift scrolling, tracking viewport focus, and keeping the published copy in sync with Hand Mode guidance.
- test: complete step [p1] Extend the FPS frontend markup assertions to cover the new navigation guard helper and refreshed control instructions.

## 2025-10-03T10:51:44Z
- fix: complete step [p1] Stabilize the orbit and MWE viewers by disabling X3D examine inertia drift via explicit NavigationInfo typeParams.
- fix: complete step [p1] Remap the FPS controller so Space lifts and Shift descends while damping vertical velocity correctly.
- test: complete step [p1] Extend the frontend markup assertions to cover the updated vertical thrust math and hand mode scaffolding.
- feat: complete step [p1] Allow GLTF assets to translate on the Y axis while clamping within walkable bounds so they no longer sink through the floor.
- fix: complete step [p1] Auto-hide the walk overlay whenever walk mode is inactive so editing gizmos stay visible after unlocking pointer lock.
- feat: complete step [p1] Add a Ctrl-toggle Hand Mode that pauses movement and enables mouse/WASDQE adjustments for precise object manipulation.

## 2025-10-03T04:30:00Z
- chore: complete step [p1] Relocate the Three.js modules under dev/shared/vendor/three so the FPS demo can import them locally.
- chore: complete step [p1] Stage the dozenSidedStack GLTF bundle beside the FPS prototype for relative loading.
- fix: complete step [p1] Rework interactive_3d_room_fps_demo.html to load the GLTF sample with local modules and refreshed walk/load controls.
- test: complete step [p1] Extend the FPS frontend markup assertions to cover the GLTF loader wiring and new button identifiers.

## 2025-10-03T03:45:00Z
- fix: complete step [p1] Replace the FPS importmap with explicit Three.js module URLs so blocked importmaps no longer break the controls panel.
- fix: complete step [p1] Point the FPS sample asset loader at `./dozenSidedStack-Body.x3d` so the sample import succeeds on hosted builds.
- fix: complete step [p1] Add a resnapAll helper so changing the snap grid re-aligns existing survey geometry before re-rendering.

## 2025-10-03T02:20:00Z
- fix: complete step [p1] Trace why the FPS viewer walk/reset buttons stalled by surfacing pointer-lock failures, disabling walk mode when unsupported, and updating the HUD messaging.
- fix: complete step [p1] Restore the first-person camera anchor by clearing move state on layout loads, pointer-lock unlocks, and resets so the scene stops drifting toward the viewer.
- test: extend frontend markup checks to ensure the FPS demo ships the walk status element, resetMovementState helper, and pointer-lock error handler wiring.

## 2025-10-03T01:35:44Z
- fix: complete step [p1] Reproduce the `default_room.json` import failure and harden the parser with a fallback slice so legacy exports no longer trigger the generic alert.
- fix: complete step [p1] Update the orbit viewer loader to preserve furniture transforms by normalizing incoming layout payloads instead of resetting to presets.
- feat: complete step [p1] Add a themed MWE viewer tab with the dozen-sided stack inline asset so the baseline X3D runtime stays verifiable on the hosted server.
- feat: tighten the 2D survey initialization to restore layouts from `/api/layout` or local storage and persist edits with throttled saves for cross-tab continuity.
- test: extend frontend markup checks to cover the new MWE navigation link and ensure the 2D survey references the shared layout persistence key.

## 2025-10-03T00:58:56Z
- fix: complete step [p1] Compare the orbit viewer markup against the working X3D MWE to pinpoint missing runtime namespace usage.
- fix: complete step [p1] Refactor interactive_3d_room_v1.html to create X3D nodes with document.createElementNS so room geometry renders.
- test: complete step [p1] Guard the namespace helper by asserting interactive_3d_room_v1.html references createX3DElement for key X3D tags.

## 2025-10-03T01:10Z
- fix: complete step [p1] Investigate why the FPS viewer prototype was not persisting imported layouts and confirm server storage paths.
- feat: complete step [p1] Implement layout persistence (local storage + server sync) for the FPS viewer and trigger it after imports and resets.
- chore: Focus the WebGL canvas before requesting pointer lock so “Enter Walk Mode” reliably engages across browsers.

## 2025-10-03T00:25Z
- feat: complete step [p1] Create regression coverage for layout store resolution, environment overrides, and shutdown handling in tests/test_server.py.
- fix: complete step [p1] Normalize dev/server.py store path resolution with env/CLI overrides and eagerly prepare the persistence directory.
- fix: complete step [p1] Ensure CTRL+C shutdown invokes ThreadingTCPServer shutdown and runs on daemon worker threads for quick exit.
- feat: complete step [p2] Emit structured logging for layout reads/saves and server lifecycle events via the apim_survey.server logger.
- docs: complete step [p2] Document the APIM_SURVEY_LAYOUT_STORE override and logging behavior in dev/server.py.

## 2025-10-03T00:15Z
- fix: ✅ [p1] Capture a reference 2D export and harden the orbit viewer importer by stripping BOM/null characters and logging nested parse errors.
- fix: ✅ [p1] Wire the orbit viewer status banner to surface success/failure details when reloading the scene after imports.
- fix: ✅ [p1] Sync the first-person demo ingest path with the updated parser so walk bounds and HUD refresh after importing layouts.
- docs: ✅ [p2] Document the end-to-end workflow in README.md and point to the sample layout export.
- chore: ✅ [p2] Archive legacy prototype HTML under dev/archive/ to keep only Home, 2D Survey, Orbit Viewer, and First-Person Demo in circulation.
- docs: Added `resources/layout_samples/default_room.json` as a known-good export for testing the import pipeline.

## 2025-10-02T23-43Z
- fix: hardened orbit viewer imports to strip BOMs, unwrap nested payloads, and surface friendly errors when 2D exports are empty or malformed.
- fix: restored the first-person demo by introducing a CDN-backed Three.js import map, applying the shared glass-dark theme, and sanitizing imported layout text.
- feat: propagated the glass-dark backdrop to the landing page and 2D survey baseline for a consistent prototype suite aesthetic.
- chore: noted the export/import regression workflow so a fresh 2D export loads instantly in both orbit and first-person demos.

## 2025-10-02T12-00
- Added a shared landing page and unified navigation styling across the survey, orbit, and first-person demos using the glass light theme.
- Preloaded the microscope room layout across 2D and 3D experiences, preventing delete-key conflicts while editing form controls.
- Synced the first-person demo with the default preset and cleared selections when importing or resetting layouts for smoother testing.

## 2025-10-02T14-00
- Added grid-snapped wall and door editing, wall edge labels, and delete-key support to `room_survey_min_v1.html` for a clearer custom-layout workflow.
- Captured the translucent "glass light" UI treatment as `dev/shared/styles/glass_light_theme.css` and wired it into the first-person 3D demo, along with control tips.
- Hardened `interactive_3d_room_fps_demo.html` for broader browser compatibility and added Ctrl-drag orbiting while outside walk mode.

## 2025-10-02
- feat: complete step [p1] Audit `interactive_3d_room_v1.html` – corrected navigation mode and viewport styling to keep the scene from free-falling on load.
- feat: complete step [p1] Restore orbit viewer buttons – rewired Apply/Home actions to refresh the scene, reset the camera, and surface status feedback.
- feat: complete step [p1] Add explicit Save and Load controls – introduced UI buttons, status messaging, and snapshot helpers to persist layouts.
- feat: complete step [p1] Stand up a minimal Python HTTP server – added a threaded standard-library server with JSON persistence endpoints and tests.
- feat: complete step [p2] Apply shared glass-light dark theme tokens – overhauled the orbit viewer styling and background to match the suite’s dark treatment.
- feat: complete step [p2] Persist layout data client-side – synced localStorage restores with imports and automatic saves when the viewer loads or updates.
# Changelog

## 2025-10-06T05:30:00Z
- fix: complete step [p1] Wire orientation tab clicks to update the SVG data attribute so wall and ceiling projections replace the floor plan without losing selection context.
- feat: complete step [p2] Gate the survey scale overlay behind a config flag and documentable tests so rulers render without blocking interactions.
- docs: Refine the design-principles Q&A to emphasize custom notes, follow-up integration, and sensor context.
- test: Extend markup assertions to cover the SVG orientation attribute setter and the FPV human eye-height constant.
