import {
  BufferGeometry,
  TriangleFanDrawMode,
  TriangleStripDrawMode
} from './three.module.js';

function toTrianglesDrawMode(geometry, drawMode) {
  if (!geometry || !(geometry instanceof BufferGeometry)) {
    console.warn('BufferGeometryUtils: toTrianglesDrawMode expects a BufferGeometry.');
    return geometry;
  }

  if (drawMode === TriangleStripDrawMode) {
    return convertStripToTriangles(geometry);
  }

  if (drawMode === TriangleFanDrawMode) {
    return convertFanToTriangles(geometry);
  }

  return geometry;
}

function convertStripToTriangles(source) {
  const geometry = source.clone();
  const index = geometry.getIndex();
  const nextIndices = [];

  if (index) {
    const original = index.array;
    for (let i = 2; i < original.length; i += 1) {
      const a = original[i - 2];
      const b = original[i - 1];
      const c = original[i];
      if (i % 2 === 0) {
        nextIndices.push(a, b, c);
      } else {
        nextIndices.push(b, a, c);
      }
    }
  } else {
    const position = geometry.attributes.position;
    if (!position) {
      return geometry;
    }
    for (let i = 2; i < position.count; i += 1) {
      const a = i - 2;
      const b = i - 1;
      const c = i;
      if (i % 2 === 0) {
        nextIndices.push(a, b, c);
      } else {
        nextIndices.push(b, a, c);
      }
    }
  }

  geometry.setIndex(nextIndices);
  geometry.clearGroups();
  geometry.addGroup(0, nextIndices.length, 0);
  return geometry;
}

function convertFanToTriangles(source) {
  const geometry = source.clone();
  const index = geometry.getIndex();
  const nextIndices = [];

  if (index) {
    const original = index.array;
    if (original.length < 3) {
      return geometry;
    }
    const firstIndex = original[0];
    for (let i = 1; i < original.length - 1; i += 1) {
      const b = original[i];
      const c = original[i + 1];
      nextIndices.push(firstIndex, b, c);
    }
  } else {
    const position = geometry.attributes.position;
    if (!position || position.count < 3) {
      return geometry;
    }
    for (let i = 1; i < position.count - 1; i += 1) {
      nextIndices.push(0, i, i + 1);
    }
  }

  geometry.setIndex(nextIndices);
  geometry.clearGroups();
  geometry.addGroup(0, nextIndices.length, 0);
  return geometry;
}

export { toTrianglesDrawMode };
