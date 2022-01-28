# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 7_8_matplotlib_interact
Author    : Focus
Date      : 8/25/2021 11:16 PM
Keywords  : GUI, use("Agg")
Abstract  :
Param     : 
Usage     : py 7_8_matplotlib_interact
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pygame


# Sec 2
fig = plt.figure(figsize=[3, 3])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)
img = pygame.image.load("head.jpg")

#Sec 3
def plot(data):
    ax.plot(data)
    canvas.draw()
    rendered = canvas.get_renderer()

    raw_data = rendered.tostring_rgb()
    size = canvas.get_width_height()
    return pygame.image.fromstring(raw_data, size, "RGB")


#4
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Animating Objects")


#5
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


# Sec 6
i = 0
history = np.array([])
surf = plot(history)
while True:
    screen.fill((255, 255, 255))
    if i >= len(pos):
        i = 0
        surf = plot(history)
    screen.blit(img, pos[i])
    history = np.append(history, pos[i])
    screen.blit(surf, (100, 100))
    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)