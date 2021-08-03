from pygame.locals import *
import pygame
import sys

RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (233, 163, 38)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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


def drawAnswerGrid(maze, path):
    blockSize = 80
    for x in range(0, 800, blockSize):
        for y in range(0, 800, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if maze[y//80][x//80] == 1:
                SCREEN.fill(RED, rect)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
    for t in path:
        rect = pygame.Rect(t[1] * 80, t[0] * 80, blockSize, blockSize)
        SCREEN.fill(GREEN, rect)


# Calculate the shortest path


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


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
    s_e_position = []
    while True:
        SCREEN.fill(WHITE)
        drawGrid(maze)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
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
                                s_e_position.append([u//80, t//80])

        if len(s_e_position) == 2:
            start = tuple(s_e_position[0])
            end = tuple(s_e_position[1])

            maze[start[0]][start[1]] = 0
            maze[end[0]][end[1]] = 0
            path = astar(maze, start, end)
            drawAnswerGrid(maze, path)

        pygame.display.update()
"""
        for i in range(10):
            for j in range(10):
                if maze[i][j] == 2:
                    if count == 1:
                        start = (i, j)
                        print(1)
                    if count == 2:
                        end = (i, j)
                        maze[start[0]][start[1]] = 0
                        maze[end[0]][end[1]] = 0
                        print(maze)
                        path = astar(maze, start, end)
                        drawAnswerGrid(maze, path)
                        print(path)
                        break
"""
