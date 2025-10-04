import assert from 'node:assert/strict';

import { createMovementController } from '../../dev/interactive_3d_room/fpv_movement_controller.js';

const controller = createMovementController({ speed: 3.2, damping: 9.5 });

const step = (delta, pointerLocked = true) =>
  controller.step({ delta, pointerLocked });

step(0.016, false);
assert.equal(controller.velocity.x, 0);
assert.equal(controller.velocity.y, 0);
assert.equal(controller.velocity.z, 0);

controller.moveState.forward = true;
step(0.016, true);
const forwardVelocity = controller.velocity.z;
assert.notEqual(forwardVelocity, 0);

controller.moveState.forward = false;
step(0.016, true);
assert.equal(controller.velocity.z, 0);
assert.equal(controller.velocity.x, 0);
assert.equal(controller.velocity.y, 0);
assert.equal(controller.hasActiveMovement(), false);

controller.reset();
assert.equal(controller.velocity.z, 0);
assert.equal(controller.direction.x, 0);
