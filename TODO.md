TEST -- using AGENTS.md file
# TODO
✅ [p1] Remove the obsolete MWE viewer by deleting dev/test_objects/mwe_viewer.html and stripping all navigation links or tests that reference it.
✅ [p1] Excise the broken orbit viewer references from marketing copy and persistence keys so only the 2D survey and FPV flows remain.
✅ [p1] Persist placed GLTF assets across the 2D survey and FPV views by serializing placements to shared storage and restoring them when either view loads.
🔲 [p2] Extend regression tests to cover importing a saved layout and switching between tabs without losing state.
🔲 [p2] Add an automated check that first-person mode stops moving when no input is pressed.
🔲 [p2] Backfill regression coverage for the new FPS module loader path or document why automated coverage is deferred.
🔲 [p3] Catalog reusable "glass light" theme tokens for other room survey prototypes and expand the shared theme library as new looks emerge.
🔲 [p3] Evaluate additional camera input affordances (e.g., touch gestures and keyboard shortcuts) for the 3D first-person demo after the next round of feedback.
🔲 [p3] Gate the FPS "Enter Walk Mode" button when pointer lock is unsupported and surface a toast to clarify the disabled state.
