import pygame # 导入 Pygame 模块
from pygame.locals import *
def start(): # 定义一个 start 类
    screen = pygame.display.set_mode((480, 700))
    background = pygame.image.load("./Resources/background.png").convert()
    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                print("再见")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    print("←")
                if event.key == K_RIGHT or event.key == K_d:
                    print("→")
                if event.key == K_SPACE:
                    print("你按了空格")

if __name__ == '__main__':
    start()