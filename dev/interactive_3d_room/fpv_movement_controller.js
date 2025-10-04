export function createMovementController(options = {}) {
  const { speed = 3.5, damping = 10 } = options;
  const moveState = {
    forward: false,
    back: false,
    left: false,
    right: false,
    up: false,
    down: false,
  };
  const velocity = { x: 0, y: 0, z: 0 };
  const direction = { x: 0, y: 0, z: 0 };

  function hasActiveMovement() {
    return (
      moveState.forward ||
      moveState.back ||
      moveState.left ||
      moveState.right ||
      moveState.up ||
      moveState.down
    );
  }

  function reset() {
    moveState.forward = false;
    moveState.back = false;
    moveState.left = false;
    moveState.right = false;
    moveState.up = false;
    moveState.down = false;
    velocity.x = 0;
    velocity.y = 0;
    velocity.z = 0;
    direction.x = 0;
    direction.y = 0;
    direction.z = 0;
  }

  function applyDamping(delta) {
    const clampDamping = Math.max(0, damping);
    velocity.x -= velocity.x * clampDamping * delta;
    velocity.y -= velocity.y * clampDamping * delta;
    velocity.z -= velocity.z * clampDamping * delta;
  }

  function normalizeDirection() {
    const lengthSq = direction.x ** 2 + direction.y ** 2 + direction.z ** 2;
    if (lengthSq > 0) {
      const length = Math.sqrt(lengthSq);
      direction.x /= length;
      direction.y /= length;
      direction.z /= length;
      return true;
    }
    return false;
  }

  function integrate(delta) {
    const maxSpeed = Math.max(0, speed);
    if (moveState.forward || moveState.back) {
      velocity.z -= direction.z * maxSpeed * delta;
    }
    if (moveState.left || moveState.right) {
      velocity.x -= direction.x * maxSpeed * delta;
    }
    if (moveState.up || moveState.down) {
      velocity.y += direction.y * maxSpeed * delta;
    }
  }

  function step({ delta, pointerLocked }) {
    if (!pointerLocked) {
      velocity.x = 0;
      velocity.y = 0;
      velocity.z = 0;
      direction.x = 0;
      direction.y = 0;
      direction.z = 0;
      return { velocity, direction };
    }

    applyDamping(delta);

    if (hasActiveMovement()) {
      direction.z = Number(moveState.forward) - Number(moveState.back);
      direction.x = Number(moveState.right) - Number(moveState.left);
      direction.y = Number(moveState.up) - Number(moveState.down);
      if (normalizeDirection()) {
        integrate(delta);
      }
    } else {
      velocity.x = 0;
      velocity.y = 0;
      velocity.z = 0;
      direction.x = 0;
      direction.y = 0;
      direction.z = 0;
    }

    return { velocity, direction };
  }

  return {
    moveState,
    velocity,
    direction,
    hasActiveMovement,
    reset,
    step,
  };
}
