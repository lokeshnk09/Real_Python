
import pygame
from pygame.locals import *

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("A* Path Finding Algorithm")


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

screen.fill(YELLOW)
pygame.display.update()


def event():
    key_dict = {K_k: BLACK, K_r: RED, K_g: GREEN, K_b: BLUE,
                K_y: YELLOW, K_c: CYAN, K_m: MAGENTA, K_w: WHITE}
    background = GRAY
    running = True
    while running:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
            screen.fill(background)
            caption = r'(background color = ' + str(background)
            pygame.display.set_caption("A* Path Finding " + caption)
            pygame.display.update()


event()
