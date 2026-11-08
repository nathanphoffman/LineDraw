import pygame

from screen import WIDTH, HEIGHT, Screen

BLUE = (0, 0, 255)


def main():
    screen = Screen()
    clock = pygame.time.Clock()
    running = True
    x = 0
    speed = 200  # pixels per second

    while running:
        dt = clock.tick(60) / 1000 # 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x = (x + speed * dt) % WIDTH
        screen.surface.fill((0, 0, 0))
        pygame.draw.circle(screen.surface, (255, 255, 255), (int(x), 300), 20)
        screen.show()

    pygame.quit()

    #  Use pygame's font only to get a mask of "Hello World";
    # every pixel is still drawn one at a time via set_pixel.
    # font = pygame.font.Font(None, 200)
    # mask = pygame.mask.from_surface(font.render("Hello World", True, (255, 255, 255)))
    # w, h = mask.get_size()
    # x0, y0 = (WIDTH - w) // 2, (HEIGHT - h) // 2

    # for y in range(h):
        # for x in range(w):
            # if mask.get_at((x, y)):
                # screen.set_pixel(x0 + x, y0 + y, BLUE)

    # screen.show()
    # screen.wait_for_close()


if __name__ == "__main__":
    main()