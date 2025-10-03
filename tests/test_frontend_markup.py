from pathlib import Path


def test_home_nav_lists_active_demos() -> None:
    html = Path("dev/index.html").read_text(encoding="utf-8")
    assert 'href="room_survey_min/room_survey_min_v1.html"' in html
    assert 'href="interactive_3d_room/interactive_3d_room_fps_demo.html"' in html
    assert "MWE Viewer" not in html
    assert "Orbit Viewer" not in html


def test_room_survey_handles_gltf_asset_floor_item() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )
    assert "const FLOOR_ITEM_DEFS" in html
    assert "gltfAsset" in html
    assert "assetRef" in html
    assert "elevation_mm" in html


def test_layout_storage_key_shared_between_views() -> None:
    survey_html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )
    fps_html = Path(
        "dev/interactive_3d_room/interactive_3d_room_fps_demo.html"
    ).read_text(encoding="utf-8")
    expected = "const LAYOUT_STORAGE_KEY = 'apim-room.latest-layout';"
    assert expected in survey_html
    assert expected in fps_html


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


def test_fps_viewer_persists_gltf_asset_state() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "const ASSET_FLOOR_ITEM_TYPE = 'gltfAsset';" in html
    assert "function worldToLayoutFloor" in html
    assert "function syncAssetLayoutFromAnchor" in html
    assert "assetRef" in html


def test_fps_viewer_reports_asset_scale_and_recenter_controls() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "function deriveAssetScale" in html
    assert "function setAssetStatus" in html
    assert "resetAssetViewBtn" in html
    assert "setAssetStatus('Unable to load the sample GLTF file." in html


def test_room_survey_exposes_cable_controls_and_rendering() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert 'id="cableControls"' in html
    assert "const CABLE_CATALOG_URL" in html
    assert "function renderCables()" in html
    assert "cables: state.cables.map" in html


def test_room_survey_exposes_cable_bend_points() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "function insertCableBendPoint" in html
    assert "function handleCableBendDown" in html
    assert "data-bend-index" in html


def test_fps_viewer_includes_cable_catalog_and_mesh_refresh() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "const CABLE_CATALOG_URL" in html
    assert "const CABLE_COLORS" in html
    assert "async function refreshCableMeshes" in html
