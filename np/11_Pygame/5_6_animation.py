# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 5_6_animation
Author    : Focus
Date      : 8/25/2021 11:00 PM
Keywords  : static, clock
Abstract  : show different pics in different time at different position.
Param     : 
Usage     : py 5_6_animation
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys, pygame
from pygame.locals import *


#Sec 2
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Animation Object")

#Sec 3
img = pygame.image.load("head.jpg")
steps = np.linspace(20, 360, 40).astype(int)
right = np.zeros((2, len(steps)))
down = right.copy()
left = right.copy()
up = right.copy()
right[0] = steps
right[1] = 20
down[0] = 360
down[1] = steps
left[0] = steps[::-1]
left[1] = 360
up[0] = 20
up[1] = steps[::-1]
pos = np.concatenate((right.T, down.T, left.T, up.T))
i = 0
while True:
    screen.fill((255, 255, 255))
    if i >= len(pos):
        i = 0

    screen.blit(img, pos[i])
    i += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(2)

