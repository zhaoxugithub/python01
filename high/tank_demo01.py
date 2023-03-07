import pygame
import random

# 游戏界面宽度和高度
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 坦克宽度和高度
TANK_WIDTH = 32
TANK_HEIGHT = 32

# 子弹宽度和高度
BULLET_WIDTH = 4
BULLET_HEIGHT = 4

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 定义方向
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# 定义坦克类
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([TANK_WIDTH, TANK_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.speed = 2

    def move(self):
        if self.direction == UP:
            self.rect.y -= self.speed
        elif self.direction == DOWN:
            self.rect.y += self.speed
        elif self.direction == LEFT:
            self.rect.x -= self.speed
        elif self.direction == RIGHT:
            self.rect.x += self.speed

        # 如果坦克移动出屏幕，则重新设置位置和方向
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH - TANK_WIDTH or \
           self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT - TANK_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - TANK_WIDTH)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - TANK_HEIGHT)
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

# 定义子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 5

    def move(self):
        if self.direction == UP:
            self.rect.y -= self.speed
        elif self.direction == DOWN:
            self.rect.y += self.speed
        elif self.direction == LEFT:
            self.rect.x -= self.speed
        elif self.direction == RIGHT:
            self.rect.x += self.speed

        # 如果子弹移动出屏幕，则销毁子弹
        if self.rect.x < 0 or self.rect.x > SCREEN_WIDTH or \
           self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.kill()

# 初始化 Pygame
pygame.init()

# 创建游戏界面
screen = pygame.display
