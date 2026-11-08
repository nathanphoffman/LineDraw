
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

@dataclass
class Line:
    x1: float
    y1: float
    x2: float
    y2: float

def handle_line_drawing(pygame, surface, dt, elapsed):
    distance = SPEED * dt
    global CURRENT_POINT
    CURRENT_POINT = (10, int(CURRENT_POINT[1] - distance))
    pygame.draw.line(surface, LINE_COLOR, START_POINT, CURRENT_POINT)