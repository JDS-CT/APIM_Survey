export function snapValue(value, snap) {
  const step = Number(snap);
  if (!Number.isFinite(step) || step <= 0) {
    return value;
  }
  const scaled = value / step;
  const rounded = Math.round(scaled);
  return rounded * step;
}

export function snapPoint(point, snap) {
  const src = point || {};
  return {
    x: snapValue(Number(src.x) || 0, snap),
    y: snapValue(Number(src.y) || 0, snap),
  };
}

export function clampScalar(value, min = -Infinity, max = Infinity) {
  let next = value;
  if (Number.isFinite(min)) {
    next = Math.max(min, next);
  }
  if (Number.isFinite(max)) {
    next = Math.min(max, next);
  }
  return next;
}

export function applyDragSnap({ pointer, offsets, snap, limits }) {
  const src = pointer || {};
  const offset = offsets || {};
  const bounds = limits || {};
  const quantizedX = snapValue((Number(src.x) || 0) - (Number(offset.x) || 0), snap);
  const quantizedY = snapValue((Number(src.y) || 0) - (Number(offset.y) || 0), snap);
  return {
    x: clampScalar(quantizedX, bounds.minX, bounds.maxX),
    y: clampScalar(quantizedY, bounds.minY, bounds.maxY),
  };
}
