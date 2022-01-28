# -*- coding:utf-8 -*-
"""
Project   : numpy
File Name : 13_14_opengl
Author    : Focus
Date      : 8/26/2021 12:44 AM
Keywords  : OpenGL,
Abstract  :
Param     : 
Usage     : py 13_14_opengl
Reference :
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame
from pygame.locals import *
from OpenGL import *
from OpenGL.GLU import *

def display_openGL(w, h):
    pygame.display.set_mode((w, h), pygame.OPENGL(pygame.DOUBLEBUF))
