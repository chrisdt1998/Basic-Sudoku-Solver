import numpy as np
import pygame
import sys
import time
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
dim = 370
gap = 40
win = pygame.display.set_mode((dim,dim))


def start(puzzle):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        sudoku(puzzle)
        time.sleep(10)
        running = False
    pygame.quit()

def draw_lines():
    width = 10
    pygame.draw.line(win, black, (0, 0), (0, dim), width)
    pygame.draw.line(win, black, (0, dim), (dim, dim), width)
    pygame.draw.line(win, black, (dim, 0), (dim, dim), width)
    pygame.draw.line(win, black, (0, 0), (dim, 0), width)
    width = int(width/5)
    for i in range(1, 9):
        if i%3 ==0:
            pygame.draw.line(win, black, (5+(i*gap), 5), (5+(i*gap), dim-5), width*2)
            pygame.draw.line(win, black, (5, 5+(i*gap)), (dim-5, 5+(i*gap)), width*2)
        else:
            pygame.draw.line(win, black, (5+(i*gap), 5), (5+(i*gap), dim-5), width)
            pygame.draw.line(win, black, (5, 5+(i*gap)), (dim-5, 5+(i*gap)), width)

def update_puzzle(puzzle):
    font = pygame.font.SysFont("comicsans", 30, True)
    for i in range(9):
        for j in range(9):
            text = font.render(str(puzzle[i][j]), False, black)  # Arguments are: text, anti-aliasing, color
            win.blit(text, (5+int(gap/2)-7+(j*gap), 5+int(gap/2)-7+(i*gap)))


def update(puzzle):
    win.fill(white)
    draw_lines()
    update_puzzle(puzzle)
    pygame.display.update()

def sudoku(puzzle):
    puzzle_org = puzzle.copy()
    i = 0
    j = 0
    while i < 9:
        while j < 9:
            if puzzle_org[i][j] == 0:
                t = 1
                while t <= 9:
                    if t not in puzzle[:, j] and t not in puzzle[i, :]:
                        row = 3*int(i/3)
                        col = 3*int(j/3)
                        if t not in puzzle[row][col:col+3] and t not in puzzle[row+1][col:col+3] and t not in puzzle[row+2][col:col+3]:
                            puzzle[i][j] = t
                            update(puzzle)
                            # time.sleep(0.01)
                            j += 1
                            break
                    t += 1
                    if t == 10:
                        puzzle[i][j] = 0
                        update(puzzle)
                        # time.sleep(0.01)
                        # print(f"row {i}, column {j}")
                        if j > 0:
                            j -= 1
                        else:
                            i -= 1
                            j = 8
                        t = 0
                        while puzzle_org[i][j] != 0:
                            if j > 0:
                                j -= 1
                            elif i > 0:
                                i -= 1
                                j = 8
                            elif i <= 0:
                                print(puzzle)
                                raise AssertionError(f"No solution found: i = {i}, j = {j}")
                        t = puzzle[i][j]
            else:
                j += 1
        i += 1
        j = 0

    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# print(sudoku(puzzle))
# Should return
# puzzle_true = [[5,3,4,6,7,8,9,1,2],
#   [6,7,2,1,9,5,3,4,8],
#   [1,9,8,3,4,2,5,6,7],
#   [8,5,9,7,6,1,4,2,3],
#   [4,2,6,8,5,3,7,9,1],
#   [7,1,3,9,2,4,8,5,6],
#   [9,6,1,5,3,7,2,8,4],
#   [2,8,7,4,1,9,6,3,5],
#   [3,4,5,2,8,6,1,7,9]]


start(np.array(puzzle))