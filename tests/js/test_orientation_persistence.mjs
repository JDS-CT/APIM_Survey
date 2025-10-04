import assert from 'node:assert/strict';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readFile } from 'node:fs/promises';

import {
  normalizeOrientation,
  orientationKeyFromState,
  parseOrientationKey,
  snapshotOrientation,
} from '../../dev/room_survey_min/orientation_helpers.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const fixturePath = resolve(__dirname, '../fixtures/layout_orientation_fixture.json');
const layout = JSON.parse(await readFile(fixturePath, 'utf-8'));

const initialOrientation = normalizeOrientation(layout.orientation, {
  selectedSurface: layout.selected_surface,
  resolveWallRef: surface => {
    if (!surface || typeof surface !== 'object') return null;
    if (surface.type === 'wall') return surface.ref || null;
    if (surface.type === 'wallItem' && layout.wall_items) {
      const match = layout.wall_items.find(item => item.id === surface.id);
      return match ? match.wall : null;
    }
    if (surface.type === 'door' && layout.doors) {
      const match = layout.doors.find(door => door.id === surface.id);
      return match ? match.wall : null;
    }
    return null;
  },
});

assert.equal(snapshotOrientation(initialOrientation), 'wall:base:2');

const state = {
  orientation: initialOrientation,
  selectedSurface: layout.selected_surface,
  cables: layout.cables.slice(),
};

const originalCableSignature = JSON.stringify(state.cables);
const tabSequence = ['ceiling', 'floor', 'wall:base:2'];

for (const tab of tabSequence) {
  state.orientation = parseOrientationKey(tab);
  const key = orientationKeyFromState(state.orientation);
  assert.equal(typeof key, 'string');
  assert.equal(state.selectedSurface.id, layout.selected_surface.id);
  assert.equal(JSON.stringify(state.cables), originalCableSignature);
}

assert.equal(snapshotOrientation(state.orientation), 'wall:base:2');
