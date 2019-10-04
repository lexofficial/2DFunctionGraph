# Written by LeX | Draw 2D graphs 

import pygame
import sys
import random

# Colors

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
pink = (255,200,200)

colors = [red,green,blue,darkBlue,white,pink]

# Init PyGame

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.update()

# Get point data from user

icsunu = input("X1 = ")
igrecunu = input("Y1 = ")
icsdoi = input("X2 = ")
igrecdoi = input("Y2 = ")

# Converting them into int values

icsunu = int(icsunu)
icsdoi = int(icsdoi)
igrecunu = int(igrecunu)
igrecdoi = int(igrecdoi)

# Adjusting them so that they fit nicely in the middle of the graph
# !!! 10 value can be changed if you want ur graph to be able to display lines bigger than 30 units !!!

xone = 300 + icsunu * 10
yone = 300 - igrecunu * 10
xtwo = 300 + icsdoi * 10
ytwo = 300 - igrecdoi * 10

# Adding everything into a point list

pointlist = [(xone,yone),(xtwo,ytwo)]

# X, Y lines of refrence
xdreapta = [(300,2),(300,598)]
ydreapta = [(0,300),(598,300)]
pygame.draw.lines(screen, green, False, xdreapta, 3)
pygame.draw.lines(screen, green, False, ydreapta, 3)

# Drawing the plot line
pygame.draw.lines(screen, red, False, pointlist, 5)

# Drawing the A,B points
pygame.draw.circle(screen, white, (xone,yone), 4, 4)
pygame.draw.circle(screen, white, (xtwo,ytwo), 4, 4)

# Updating the screen
pygame.display.update()

# Wait for enter to close the window
input()
