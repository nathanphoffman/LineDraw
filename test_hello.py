import pygame
import random
import math

from screen import WIDTH, HEIGHT, Screen
from dataclasses import dataclass

BLUE = (0, 0, 255)
SPEED = 200
OFFSET = 10
RADIUS = 5
CIRCLE_COLOR = (255, 255, 255)
circles = []

@dataclass
class Circle:
    x: float
    y: float
    angle: float

def random_number(start,end):
    return random.randint(start,end)

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

def get_reflection_angle(circle):
    return (circle.x, circle.y)

def out_of_bounds(x, y):
    x_out_of_bounds = x > WIDTH or x < 0
    y_out_of_bounds = y > HEIGHT or y < 0
    return x_out_of_bounds or y_out_of_bounds

def get_and_set_new_position(circle, dt):
    new_x = (circle.x + SPEED * dt * math.cos(circle.angle))
    new_y = (circle.y + SPEED * dt * math.sin(circle.angle))

    if(out_of_bounds(new_x, new_y)):
        (reflection_x, reflection_y) = get_reflection_angle(circle)
        circle.x = reflection_x
        circle.y = reflection_y
    else:
        circle.x = int(new_x)
        circle.y = int(new_y)

    return (circle.x, circle.y)

def handle_bouncing_circles(surface, dt):
    for circle in circles:
        new_position = get_and_set_new_position(circle, dt)
        pygame.draw.circle(surface, CIRCLE_COLOR, new_position, RADIUS)

def main():
    screen = Screen()
    clock = pygame.time.Clock()
    running = True
    x = 0
    elapsed = 0
    ready_for_new_circle = True

    while running:
        dt = clock.tick(60) / 1000 # 60fps
        elapsed += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.surface.fill((0, 0, 0))

       
        # Every 5 seconds
        if(round(elapsed) % 5 == 0):
            if(ready_for_new_circle == True):
                ready_for_new_circle = False
                spawn_bouncing_circle()
        else:
            ready_for_new_circle = True

        handle_bouncing_circles(screen.surface, dt)
        
        screen.show()

    pygame.quit()


if __name__ == "__main__":
    main()