import pygame

from screen import WIDTH, HEIGHT, Screen
from dataclasses import dataclass
from circles import spawn_and_handle_circles
from lines import handle_line_drawing

def main():
    screen = Screen()
    clock = pygame.time.Clock()
    running = True
    x = 0
    elapsed = 0
    #current_control_direction = Direction.UP

    last_pointer_x = 20
    last_pointer_y = 20

    while running:
        dt = clock.tick(60) / 1000 # 60fps
        elapsed += dt
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.surface.fill((0, 0, 0))
        #current_control_direction = get_control_direction(pygame)       

        #render_pointer(current_control_direction)
        spawn_and_handle_circles(pygame, screen.surface, dt, elapsed)
        handle_line_drawing(pygame, screen.surface, dt, elapsed)
        # Every 5 seconds

        screen.show()

    pygame.quit()


if __name__ == "__main__":
    main()