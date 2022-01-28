# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 3_4_hello_world
Author    : Focus
Date      : 8/25/2021 10:49 PM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 3_4_hello_world
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Screen!")
pygame.display.set_caption("Screen_1!")

while True:
    sysFont = pygame.font.SysFont("None", 40)
    rendered = sysFont.render("Hello world", 0, (50, 200, 50))
    screen.blit(rendered, (200, 100))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()