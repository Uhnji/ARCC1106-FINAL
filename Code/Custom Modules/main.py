import pygame

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1280,720))

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get(): # Player Input Handler
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # Do logical updates here.
        # ...

        screen.fill("black")  # Background color

        # Render the graphics here.
        # ...

        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)