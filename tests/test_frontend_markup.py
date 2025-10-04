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
    assert "./assets/dozenSidedStack-Body.glb" in html


def test_fps_viewer_supports_hand_mode_and_vertical_translation() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "const HAND_MODE_TOGGLE_KEY" in html
    assert "let handModeTranslateStep" in html
    assert "let handModeVerticalStep" in html
    assert "transformControls.showY = true" in html
    assert "scheduleWalkOverlayAutoHide" in html
    assert "pointerControls.getObject().position.y += velocity.y * delta" in html
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
    assert "movementController.reset" in html


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

    assert "shared/scripts/cable_catalog_defaults.js" in html
    assert 'id="cableControls"' in html
    assert "const CABLE_CATALOG_URL" in html
    assert "normalizeCableCatalogWithDefaults" in html
    assert "function renderCables()" in html
    assert "cables: state.cables.map" in html
    assert 'value="gas_socket"' in html
    assert 'value="feedthrough"' in html


def test_room_survey_exposes_cable_bend_points() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "function insertCableBendPoint" in html
    assert "function handleCableBendDown" in html
    assert "data-bend-index" in html


def test_room_survey_exposes_orientation_tabs() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert 'id="orientationTabs"' in html
    assert 'data-orientation="floor"' in html
    assert 'data-orientation="ceiling"' in html
    assert 'data-orientation="wall:base:1"' in html
    assert 'id="viewSelectedWall"' in html


def test_room_survey_serializes_orientation_state() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "orientation_helpers.js" in html
    assert "snapshotOrientation" in html
    assert "normalizeOrientation" in html
    assert "setOrientation(key" in html


def test_room_survey_provides_wall_elevation_and_scale_overlay() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert 'id="wallElevationLayer"' in html
    assert 'id="scaleOverlay"' in html
    assert "function renderWallOrientation()" in html
    assert "function renderScaleOverlay()" in html
    assert "const DOOR_ELEVATION_HEIGHT_MM" in html
    assert "const SCALE_OVERLAY_CONFIG" in html


def test_room_survey_inventory_table_with_fit_checks() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert 'id="inventoryPanel"' in html
    assert 'id="inventoryTable"' in html
    assert "Microscope Fits Through Entrance?" in html
    assert "function renderInventoryTable" in html
    assert "function computeMicroscopeFitForWidth" in html


def test_wall_elevation_uses_shared_snap_drag_pipeline() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "function handleWallElevationDragStart" in html
    assert "drag.kind === 'wall-elevation-item'" in html
    assert "snapValue(roomPt.x - drag.offsetX)" in html


def test_room_survey_updates_svg_orientation_attribute() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "svg.setAttribute('data-orientation'" in html
    assert "function setOrientation(" in html


def test_fps_viewer_includes_cable_catalog_and_mesh_refresh() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "shared/scripts/cable_catalog_defaults.js" in html
    assert "const CABLE_CATALOG_URL" in html
    assert "normalizeCableCatalogWithDefaults" in html
    assert "async function refreshCableMeshes" in html
    assert "const CABLE_SAMPLE_SEGMENTS" in html


def test_fps_viewer_uses_human_scale_height_and_markers() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "const ROOM_HEIGHT_MM = 3000" in html
    assert "const scaleMarkerGroup" in html
    assert "function buildScaleMarkers" in html
    assert "function createLabelSprite" in html
    assert "const HUMAN_EYE_HEIGHT_M" in html
    assert "1.6" in html  # human-scale eye height tightened to ~1.6 m
    assert "camera.position.set(0, HUMAN_EYE_HEIGHT_M, 5);" in html


def test_fps_viewer_imports_shared_movement_controller() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "fpv_movement_controller.js" in html
    assert "createMovementController" in html
    assert "movementController.step" in html


def test_room_survey_exposes_wall_mount_height_controls() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert 'id="wallItemControls"' in html
    assert 'id="wallItemMountHeight"' in html
    assert 'id="wallItemMountHeightSlider"' in html
    assert "function updateWallItemControls" in html


def test_room_survey_exports_unclamped_cable_points() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "const rawU = Number(pt.x) / state.Wmm;" in html
    assert "const rawV = Number(pt.y) / state.Lmm;" in html
    assert "const rawW = Number(pt.z || 0) / DEFAULT_ROOM_HEIGHT_MM;" in html


def test_cable_defaults_drop_to_ground_run() -> None:
    html = Path("dev/room_survey_min/room_survey_min_v1.html").read_text(
        encoding="utf-8"
    )

    assert "const GROUND_Z_MM = 0;" in html
    assert "const CABLE_DROP_FRACTION" in html
    assert "const CABLE_DROP_MAX_MM" in html


def test_fps_viewer_syncs_layout_storage_updates() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "function handleLayoutStorageEvent" in html
    assert "window.addEventListener('storage', handleLayoutStorageEvent);" in html


def test_fps_viewer_respects_wall_mount_heights() -> None:
    html = Path("dev/interactive_3d_room/interactive_3d_room_fps_demo.html").read_text(
        encoding="utf-8"
    )

    assert "mountHeight_mm" in html
    assert "const fallbackMount" in html
