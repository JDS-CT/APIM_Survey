TEST -- using AGENTS.md file
# TODO
✅ [p1] Reproduce the `default_room.json` layout load failure and capture console/network logs for the orbit viewer import.
✅ [p1] Update the orbit viewer loader so `default_room.json` rehydrates furniture transforms instead of resetting to the origin.
✅ [p1] Add a second tab in `dev/index.html` that mounts the existing MWE viewer with the shared survey theme applied.
✅ [p1] Trace why the FPS viewer "Enter Walk Mode" and "Reset" buttons no longer activate and document the failing events.
✅ [p1] Restore first-person controls so the camera stays anchored (no unintended forward drift) when loading room layouts.
🔲 [p2] Extend regression tests to cover importing a saved layout and switching between tabs without losing state.
🔲 [p2] Add an automated check that first-person mode stops moving when no input is pressed.
🔲 [p3] Catalog reusable "glass light" theme tokens for other room survey prototypes and expand the shared theme library as new looks emerge.
🔲 [p3] Evaluate additional camera input affordances (e.g., touch gestures and keyboard shortcuts) for the 3D first-person demo after the next round of feedback.
