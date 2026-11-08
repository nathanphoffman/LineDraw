
import math

from globals import SPEED
from dataclasses import dataclass
from screen import WIDTH, HEIGHT
from utils import random_number

@dataclass
class Circle:
    x: float
    y: float
    angle: float

OFFSET = 10
RADIUS = 5
CIRCLE_COLOR = (255, 255, 255)

circles = []
READY_FOR_NEW_CIRCLE = True

def spawn_and_handle_circles(pygame, screen_surface, dt, elapsed):
    global READY_FOR_NEW_CIRCLE
    if(round(elapsed) % 5 == 0):
        if(READY_FOR_NEW_CIRCLE == True):
            READY_FOR_NEW_CIRCLE = False
            spawn_bouncing_circle()
    else:
        READY_FOR_NEW_CIRCLE = True

    handle_bouncing_circles(pygame, screen_surface, dt)


def spawn_bouncing_circle():
    center_x = WIDTH/2
    center_y = HEIGHT/2

    x_offset = random_number(0,10)
    y_offset = random_number(0,10)

    angle_degrees = random_number(0,360)
    angle = math.radians(angle_degrees)

    x = center_x + x_offset
    y = center_y + y_offset

    circles.append(Circle(x,y,angle))


def get_and_set_new_position(circle, dt):
    new_x = (circle.x + SPEED * dt * math.cos(circle.angle))
    new_y = (circle.y + SPEED * dt * math.sin(circle.angle))

    x_out_of_bounds = new_x > WIDTH or new_x < 0
    y_out_of_bounds =  new_y > HEIGHT or new_y < 0

    if(x_out_of_bounds and y_out_of_bounds):
        circle.angle = math.pi + circle.angle
        return get_and_set_new_position(circle, dt)

    elif(x_out_of_bounds):
        circle.angle = math.pi - circle.angle
        return get_and_set_new_position(circle, dt)

    elif(y_out_of_bounds):
        circle.angle = -circle.angle
        return get_and_set_new_position(circle, dt)

    else:
        circle.x = int(new_x)
        circle.y = int(new_y)

    return (circle.x, circle.y)

def handle_bouncing_circles(pygame, surface, dt):
    for circle in circles:
        new_position = get_and_set_new_position(circle, dt)
        pygame.draw.circle(surface, CIRCLE_COLOR, new_position, RADIUS)