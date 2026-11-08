
import math

from globals import SPEED
from dataclasses import dataclass
from screen import WIDTH, HEIGHT
from utils import random_number
from controls import get_control_direction, Direction


lines = []

CURRENT_POINT = (10,HEIGHT)
START_POINT = (10,HEIGHT)
LINE_COLOR = (0,0,255)
PRIOR_DIRECTION = Direction.UP

@dataclass
class Line:
    start: tuple[float,float]
    end: tuple[float,float]

def get_new_point(x_delta, y_delta):
    new_x = CURRENT_POINT[0] + x_delta
    new_y = CURRENT_POINT[1] + y_delta

    if new_x < 0:
        new_x = 0
    elif new_x > WIDTH:
        new_x = WIDTH

    if new_y < 0:
        new_y = 0
    elif new_y > HEIGHT:
        new_y = HEIGHT

    return (new_x, new_y)

def render_past_lines(pygame, surface):
    for line in lines:
        pygame.draw.line(surface, LINE_COLOR, line.start, line.end)


def get_xy_delta(direction, distance):
    y_delta = 0
    x_delta = 0

    match direction:
        case Direction.UP:
            y_delta += -distance
        case Direction.DOWN:
            y_delta += distance
        case Direction.RIGHT:
            x_delta += distance
        case Direction.LEFT:
            x_delta += -distance

    return (x_delta, y_delta)


def handle_line_drawing(pygame, surface, dt, elapsed):

    global START_POINT
    global PRIOR_DIRECTION
    direction = get_control_direction(pygame)
    direction = PRIOR_DIRECTION if direction == None else direction
    distance = SPEED * dt

    render_past_lines(pygame, surface)

    # if the user doesnt move their keys it always moves in prior direction
    if direction is PRIOR_DIRECTION:
        (x_delta, y_delta) = get_xy_delta(direction, distance)
        global CURRENT_POINT
        CURRENT_POINT = get_new_point(x_delta, y_delta)
        pygame.draw.line(surface, LINE_COLOR, START_POINT, CURRENT_POINT)
    
    else:
        lines.append(Line(START_POINT,CURRENT_POINT))
        START_POINT = CURRENT_POINT
        PRIOR_DIRECTION = direction
        
        


