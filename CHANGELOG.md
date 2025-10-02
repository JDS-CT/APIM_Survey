# Changelog

## 2024-05-09
- Added a shared landing page and unified navigation styling across the survey, orbit, and first-person demos using the glass light theme.
- Preloaded the microscope room layout across 2D and 3D experiences, preventing delete-key conflicts while editing form controls.
- Synced the first-person demo with the default preset and cleared selections when importing or resetting layouts for smoother testing.

## 2024-05-08
- Added grid-snapped wall and door editing, wall edge labels, and delete-key support to `room_survey_min_v1.html` for a clearer custom-layout workflow.
- Captured the translucent "glass light" UI treatment as `dev/shared/styles/glass_light_theme.css` and wired it into the first-person 3D demo, along with control tips.
- Hardened `interactive_3d_room_fps_demo.html` for broader browser compatibility and added Ctrl-drag orbiting while outside walk mode.
