import random
import sys
import pygame

black = 0, 0, 0
skin = pygame.image.load('skin.png')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Create an 500x500 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

clock = pygame.time.Clock()


def main():
    pygame.init()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            screen.fill(black)
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)

            pygame.display.flip()
            clock.tick(50)


if __name__ == '__main__':
    main()