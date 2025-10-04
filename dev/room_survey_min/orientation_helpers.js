export function parseOrientationKey(key) {
  if (typeof key !== 'string' || !key) {
    return { type: 'floor' };
  }
  if (key === 'floor') return { type: 'floor' };
  if (key === 'ceiling') return { type: 'ceiling' };
  if (key.startsWith('wall:')) {
    const ref = key.slice(5);
    return ref ? { type: 'wall', ref } : { type: 'wall' };
  }
  return { type: 'floor' };
}

export function orientationKeyFromState(orientation) {
  if (!orientation || typeof orientation !== 'object') {
    return 'floor';
  }
  if (orientation.type === 'ceiling') return 'ceiling';
  if (orientation.type === 'wall') {
    const ref = orientation.ref || '';
    return ref ? `wall:${ref}` : 'wall';
  }
  return 'floor';
}

export function snapshotOrientation(orientation) {
  return orientationKeyFromState(orientation);
}

function coerceWallRef(ref) {
  if (ref === null || ref === undefined) return null;
  if (typeof ref === 'number') return `base:${ref}`;
  if (typeof ref === 'string') {
    if (/^\d$/.test(ref)) {
      return `base:${ref}`;
    }
    return ref;
  }
  return null;
}

export function normalizeOrientation(input, options = {}) {
  const { selectedSurface = null, resolveWallRef = null, fallback = { type: 'floor' } } = options;

  if (input && typeof input === 'object') {
    if (input.type === 'ceiling') {
      return { type: 'ceiling' };
    }
    if (input.type === 'floor') {
      return { type: 'floor' };
    }
    if (input.type === 'wall') {
      const ref = coerceWallRef(input.ref);
      return ref ? { type: 'wall', ref } : { type: 'wall' };
    }
  }

  if (typeof input === 'string') {
    return parseOrientationKey(input);
  }

  if (typeof resolveWallRef === 'function' && selectedSurface) {
    const derived = resolveWallRef(selectedSurface);
    const ref = coerceWallRef(derived);
    if (ref) {
      return { type: 'wall', ref };
    }
  }

  return { ...fallback };
}
