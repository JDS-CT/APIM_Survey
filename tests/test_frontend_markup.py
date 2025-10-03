from pathlib import Path


def test_orbit_viewer_uses_x3d_namespace() -> None:
    html_path = Path("dev/interactive_3d_room/interactive_3d_room_v1.html")
    html = html_path.read_text(encoding="utf-8")

    assert "createElementNS" in html

    for tag in ["Coordinate", "Shape", "Appearance", "Material", "Box", "Transform"]:
        assert f"createX3DElement('{tag}')" in html


def test_orbit_and_mwe_viewers_disable_examine_drift() -> None:
    orbit_html = Path("dev/interactive_3d_room/interactive_3d_room_v1.html").read_text(
        encoding="utf-8"
    )
    mwe_html = Path("dev/test_objects/mwe_viewer.html").read_text(encoding="utf-8")

    expected = 'typeParams="1 0 0 0 0 0"'

    assert expected in orbit_html
    assert expected in mwe_html


def test_home_nav_includes_mwe_tab() -> None:
    html = Path("dev/index.html").read_text(encoding="utf-8")
    assert 'href="test_objects/mwe_viewer.html"' in html
    assert ">MWE Viewer<" in html


def test_room_survey_references_layout_persistence() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )
    assert "LAYOUT_STORAGE_KEY" in html
    assert "/api/layout" in html


def test_fps_viewer_handles_pointer_lock_state() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )
    assert 'class="control-status"' in html
    assert 'id="assetStatus"' in html
    assert "function resetMovementState()" in html
    assert "pointerlockerror" in html
    assert 'id="enter-walk"' in html
    assert 'id="load-gltf"' in html
    assert 'id="resetAssetView"' in html
    assert "../shared/vendor/three/GLTFLoader.js" in html
    assert "./assets/dozenSidedStack-Body.gltf" in html


def test_fps_viewer_supports_hand_mode_and_vertical_translation() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "const HAND_MODE_TOGGLE_KEY" in html
    assert "let handModeTranslateStep" in html
    assert "let handModeVerticalStep" in html
    assert "transformControls.showY = true" in html
    assert "scheduleWalkOverlayAutoHide" in html
    assert "velocity.y += direction.y * speed * delta" in html
    assert "selectedObject.position.y -= verticalStep" in html


def test_fps_viewer_traps_space_scroll_and_updates_controls_copy() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "function maybePreventNavigationKey" in html
    assert "Press <strong>Ctrl</strong> to toggle <strong>Hand Mode</strong>" in html
    assert "Hold <strong>Alt</strong> and drag" in html


def test_fps_viewer_exposes_translation_snap_controls() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert 'id="translationSnap"' in html
    assert 'id="translationSnapValue"' in html
    assert "function applyTranslationSnap" in html
    assert "transformControls.setTranslationSnap(translationSnap);" in html
    assert "function hasActiveMovement()" in html


def test_fps_viewer_reports_asset_scale_and_recenter_controls() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "function deriveAssetScale" in html
    assert "function setAssetStatus" in html
    assert "resetAssetViewBtn" in html
    assert "setAssetStatus('Unable to load the sample GLTF file." in html
