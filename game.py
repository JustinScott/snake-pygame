import random
import sys
import pygame

WHITE = (255, 255, 255)
BLACK = 0, 0, 0
YELLOW = 255, 255, 0

skin = pygame.image.load('skin.png')

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

PELLET_RADIUS = 10
SEGMENT_LENGTH = 20

# Create an 500x500 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


def main():
    pygame.init()

    clock = pygame.time.Clock()

    dir_vect = 1, 0
    snake = Snake()
    food = Food()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir_vect = -1, 0
                if event.key == pygame.K_RIGHT:
                    dir_vect = 1, 0
                if event.key == pygame.K_UP:
                    dir_vect = 0, -1
                if event.key == pygame.K_DOWN:
                    dir_vect = 0, 1

        if pygame.sprite.spritecollide(snake.head, food, 1):
            snake.grow()

        screen.fill(BLACK)
        snake.move(dir_vect[0], dir_vect[1])
        snake.draw(screen)
        food.draw(screen)
        pygame.display.flip()
        clock.tick(7)


MAX_FOOD = 5


class Food(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.populate()

    def populate(self):
        for _ in range(MAX_FOOD - self.count):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)

            self.add(Pellet(self, x, y))
            self.count += 1

    def draw(self, surface):
        for s in self.spritedict.items():
            pygame.draw.circle(surface,
                               YELLOW,
                               (s[0].rect.x + PELLET_RADIUS, s[0].rect.y + PELLET_RADIUS),
                               PELLET_RADIUS)
            # pygame.draw.rect(surface, WHITE, s[0].rect, 1)


class Pellet(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group)
        self.rect = pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)

    def kill(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        # self.rect = pygame.draw.circle(screen, (255, 255, 255), (x, y), 10)


def game_over():
    pass


class Snake(pygame.sprite.RenderPlain):
    def __init__(self):
        self.head = Segment(20, 20)
        self.tail = self.head
        super().__init__(self.head)

    def grow(self):
        new_segment = Segment(self.tail.rect.x, self.tail.rect.y)
        self.tail.next_segment = new_segment
        self.tail = new_segment
        self.add(new_segment)

    def move(self, x, y):
        if (x < 0 or x > SCREEN_WIDTH) or (y < 0 or y > SCREEN_HEIGHT):
            return False
        self.head.move(self.head.rect.x + x * SEGMENT_LENGTH, self.head.rect.y + y * SEGMENT_LENGTH)
        return True


class Segment(pygame.sprite.Sprite):
    next_segment = None

    def __init__(self, x, y):
        super().__init__()

        self.image = skin
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        if self.next_segment:
            self.next_segment.move(self.rect.x, self.rect.y)
        self.rect.x = x
        self.rect.y = y


if __name__ == '__main__':
    main()
