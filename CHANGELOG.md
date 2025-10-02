# Changelog

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
