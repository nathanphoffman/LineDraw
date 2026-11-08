from enum import Enum, auto

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

def get_control_direction(pygame):
    keys = pygame.key.get_pressed()

    left = keys[pygame.K_LEFT] or keys[pygame.K_a]
    right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
    up = keys[pygame.K_UP] or keys[pygame.K_w]
    down = keys[pygame.K_DOWN] or keys[pygame.K_s]

    if left:
       return Direction.LEFT
    if right:
       return Direction.RIGHT
    if up:
        return Direction.UP
    if down:
        return Direction.DOWN
    