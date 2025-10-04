# APIM Survey Prototype Workspace

This workspace hosts the microscope room planning prototypes that move from 2D
layout capture to 3D review. Everything you need to run the current iteration
lives under `dev/`, and the landing page links to the three supported flows:

* **Home** (`dev/index.html`) &mdash; overview and navigation hub.
* **2D Survey** (`dev/room_survey_min/room_survey_min_v1.html`) &mdash; capture room
  dimensions, equipment, sockets, walls, and doors.
* **First-Person Demo**
  (`dev/interactive_3d_room/interactive_3d_room_fps_demo.html`) &mdash; walk the
  space with WASD controls, place sample 3D assets, and review survey changes
  in-context.

Retired experiments (including the orbiting X3D viewer and MWE) now live in
`dev/archive/` to keep the navigation focused.

## Design Principles

**Why make this instead of simply using FreeCAD in the first place?**
FreeCAD is not installed on every company workstation, and the survey workflow
needs to run in any modern browser without extra provisioning. Delivering a
focused web experience lets surveyors capture measurements, embed custom notes,
and trigger follow-up tasks directly in a purpose-built UI while still exporting
data that other systems can consume. It keeps the scope limited to survey needs
while leaving heavyweight CAD adjustments to downstream tools.

**Why not simply use the company CAD drawings of the system to provide one
example room layout to customers?**  
Shipping a single canonical layout discourages teams from validating their own
spaces. Repeated installations have shown that facilities often discover power,
HVAC, or clearance issues only after technicians arrive, turning "simple"
installations into costly rework. Collecting detailed room data early takes a
few extra minutes during surveys but routinely prevents follow-up visits,
replacement parts, and multi-day delays that can easily exceed $10,000. The
prototype encourages collaborative review, captures context such as temporary
sensor placements, and surfaces issues before the install truck leaves the dock.

## Running the prototype server

The Python standard-library server in `dev/server.py` serves the entire `dev/`
directory and persists layouts to disk. From the repository root:

```bash
python dev/server.py
```

You should see output similar to:

```
Serving prototypes on http://127.0.0.1:5000/ (layout store: dev/data/saved_layout.json)
```

Open that URL in a browser to access the landing page and linked prototypes. The
server exposes a simple JSON API at `/api/layout` that the First-Person Demo uses
to save and restore layouts (`GET` returns the last saved payload, `POST`
persists the provided JSON object).

## 2D &rarr; 3D workflow

1. Launch the 2D Survey from the home page, adjust the room and equipment, and
   click **Export JSON**. The browser downloads `room_survey.json`.
2. Visit the First-Person Demo, click **Import 2D Layout JSON**, and choose that
   JSON file to update the walkthrough and collision bounds.
3. Use **Save Layout** in either view to write the current snapshot to the
   server (persisted at `dev/data/saved_layout.json`).

If you need a known-good file for testing, `resources/layout_samples/default_room.json`
matches the default survey preset.

## Inventory summary & clearance checks

The 2D survey sidebar now includes an **Inventory & Fit Checks** table so survey
teams can rename walls, doors, and large equipment while reviewing critical
dimensions in one place. Each row lists the item type, height, width, and length
straight from the layout store, plus derived columns for system-versus-door
clearance. Door widths populate automatically and microscopes compare their
physical width against the widest available doorway to surface a boolean
**Microscope Fits Through Entrance?** indicator. Renaming happens in-line and the
changes persist with the rest of the layout snapshot.

Derived measurements live in dedicated helpers (e.g.,
`computeMicroscopeFitForWidth`) so additional clearance checks can slot into the
table without rewriting the UI plumbing. As new equipment requirements emerge,
extend those helpers or introduce new ones and add a matching table column to
surface the comparison.
