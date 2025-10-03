# Changelog

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
