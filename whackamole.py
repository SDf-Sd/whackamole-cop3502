import pygame
from random import randrange
from pygame import Color

TILE_SIZE = 32
WIDTH, HEIGHT = 20, 16


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")

        mole_grid_pos = pygame.Vector2(randrange(0, WIDTH), randrange(0, HEIGHT))

        screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
        clock = pygame.time.Clock()
        running = True
        while running:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gx, gy = event.pos
                    gx //= TILE_SIZE
                    gy //= TILE_SIZE
                    if (mole_grid_pos == (gx, gy)):
                        mole_grid_pos.x = randrange(0, WIDTH)
                        mole_grid_pos.y = randrange(0, HEIGHT)
            screen.fill("light green")
            for i in range(WIDTH):
                pygame.draw.line(screen, Color(0, 0, 0), (i * TILE_SIZE, 0), (i * TILE_SIZE, HEIGHT * TILE_SIZE))
            for j in range(HEIGHT):
                pygame.draw.line(screen, Color(0, 0, 0), (0, j * TILE_SIZE), (WIDTH * TILE_SIZE, j * TILE_SIZE))
            
            screen.blit(mole_image, mole_image.get_rect(topleft=mole_grid_pos*TILE_SIZE))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
