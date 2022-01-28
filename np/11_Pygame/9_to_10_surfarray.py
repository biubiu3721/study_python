# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 9_to_10_surfarray
Author    : Focus
Date      : 8/25/2021 11:35 PM
Keywords  : surfarray,
Abstract  : PygameSurface<-> NumPy
Param     :
Usage     : py 9_to_10_surfarray
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame
from pygame.locals import *
import numpy as np
pygame.init()
img = pygame.image.load("head.jpg")
pixels = pygame.surfarray.array2d(img)
print("pixel:", type(pixels))
X = pixels.shape[0] * 7
Y = pixels.shape[1] * 7

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Surfarray Demo")
new_pixels = np.tile(pixels, (7, 7)).astype(int)
while True:
    screen.fill((255, 255, 255))
    pygame.surfarray.blit_array(screen, new_pixels)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
