import pygame

WIDTH, HEIGHT = 1024, 768


class Screen:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface.fill((0, 0, 0))

    def set_pixel(self, x, y, color):
        self.surface.set_at((x, y), color)

    def show(self):
        pygame.display.flip()

    def wait_for_close(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

