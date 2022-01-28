# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 11_to_12_ai_scikit_learn
Author    : Focus
Date      : 8/25/2021 11:44 PM
Keywords  : scikit-learn
Abstract  :
Param     : 
Usage     : py 11_to_12_ai_scikit_learn
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import sklearn.cluster
import pygame
from pygame.locals import *
from sklearn.cluster import AffinityPropagation


# Section 2
positions = np.random.randint(0, 400, size=(30, 2))
positions_norms = np.sum(positions ** 2, axis=1)
S = - positions_norms[:, np.newaxis] - positions_norms[np.newaxis, :] + 2 * np.dot(positions, positions.T)
aff_pro = AffinityPropagation().fit(S)
labels = aff_pro.labels_

polygon_points = []
print("max(labels)", max(labels))
for i in range(max(labels)):
    polygon_points.append([])

for i in range(len(labels)):
    print(i)
    print("label[i]", labels[i])
    polygon_points[labels[i] - 1].append(positions[i])

pygame.init()
screen = pygame.display.set_mode((400, 400))
print(polygon_points)


#polygon_points = [[0,0],[1,1],[2,3], [100,50], [100,100]]
while True:
    for i in range(len(polygon_points)):
        pygame.draw.polygon(screen, (255, 0, 0), polygon_points[i])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    pygame.display.update()

