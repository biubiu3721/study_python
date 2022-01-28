# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 15_16_conway_game_life
Author    : Focus
Date      : 8/26/2021 12:56 AM
Keywords  : 
Abstract  :
Param     : 
Usage     : py 15_16_conway_game_life
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame
import os
from pygame.locals import *
from scipy import ndimage


def get_pixar(arr, weights):
    states = ndimage.convolve(arr, weights, mode=wrap)
    bools = (states==13) | (states==12) | (states == 3)
    return bools.astype(int)

def draw_cross(pixar):
    (posx, posy) = pygame.mouse.get_pos()
    pixar[posx, :] = 1
    pixar[: posy] = 1


def random_init(n):
    return np.random.rand_integers(0, 1, (n, n))


def draw_pattern(pixar, pattern):
    print(pattern)
    if pattern == "glider":
        coords = [(0,1), (1, 2), (2, 0), (2,  1), (2,2)]
    elif pattern == "block":
        coords = [(3, 3), (3, 2), (2, 3), (2, 2)]
    elif pattern == "exploder":
        coords = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 3)]
    elif pattern == "fpentomino":
        coords = [(2, 3), (3, 2), (4, 2), (3, 3), (3, 4)]
pos = pygame.mouse.get_pos()

xs = np.arange(0, pos[0], 10)
ys = np.arange(0, pos[1], 10)


