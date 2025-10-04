import assert from 'node:assert/strict';
import { applyDragSnap, snapPoint, snapValue } from '../../dev/room_survey_min/drag_snap.js';

const SNAP = 100;

{
  const value = snapValue(1437, SNAP);
  assert.equal(value, 1400);
}

{
  const point = snapPoint({ x: 1437, y: 286 }, SNAP);
  assert.deepEqual(point, { x: 1400, y: 300 });
}

{
  const result = applyDragSnap({
    pointer: { x: 612, y: 1478 },
    offsets: { x: 12, y: 28 },
    snap: SNAP,
    limits: { minX: 0, maxX: 4000, minY: 0, maxY: 3000 },
  });
  assert.deepEqual(result, { x: 600, y: 1500 });
}

{
  const result = applyDragSnap({
    pointer: { x: -120, y: 4120 },
    offsets: { x: 0, y: 0 },
    snap: SNAP,
    limits: { minX: 0, maxX: 2500, minY: 0, maxY: 3000 },
  });
  assert.deepEqual(result, { x: 0, y: 3000 });
}

{
  const raw = applyDragSnap({
    pointer: { x: 512.5, y: 612.5 },
    offsets: { x: 12.5, y: 12.5 },
    snap: 0,
    limits: { minX: 0, maxX: 1000, minY: 0, maxY: 1000 },
  });
  assert.deepEqual(raw, { x: 500, y: 600 });
}
