import pygame
from pygame import *
import pygame
import sys

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (233, 163, 38)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800


def drawGrid(maze):
    blockSize = 80
    for x in range(0, 800, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if maze[y//80][x//80] == 1:
                SCREEN.fill(RED, rect)
            elif maze[y//80][x//80] == 2:
                SCREEN.fill(ORANGE, rect)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == "__main__":
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    while True:
        SCREEN.fill(WHITE)  # 画面を黒で塗りつぶす
        drawGrid(maze)

        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    for t in range(0, 800, 80):
                        for u in range(0, 800, 80):
                            if x > t and x <= t+80 and y > u and y <= u+80:
                                maze[u//80][t//80] = 1

                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    for t in range(0, 800, 80):
                        for u in range(0, 800, 80):
                            if x > t and x <= t+80 and y > u and y <= u+80:
                                maze[u//80][t//80] = 2

        pygame.display.update()
