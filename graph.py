# Written by LeX | Draw 2D graphs 

import pygame
import sys
import random

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
pink = (255,200,200)

colors = [red,green,blue,darkBlue,white,pink]

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.update()


icsunu = input("X1 = ")
igrecunu = input("Y1 = ")
icsdoi = input("X2 = ")
igrecdoi = input("Y2 = ")

icsunu = int(icsunu)
icsdoi = int(icsdoi)
igrecunu = int(igrecunu)
igrecdoi = int(igrecdoi)

xone = 300 + icsunu * 10
yone = 300 - igrecunu * 10
xtwo = 300 + icsdoi * 10
ytwo = 300 - igrecdoi * 10

pointlist = [(xone,yone),(xtwo,ytwo)]

xdreapta = [(300,2),(300,598)]
ydreapta = [(0,300),(598,300)]

pygame.draw.lines(screen, green, False, xdreapta, 3)
pygame.draw.lines(screen, green, False, ydreapta, 3)


pygame.draw.lines(screen, red, False, pointlist, 5)

pygame.display.update()


input()
