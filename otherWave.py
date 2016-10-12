'''
Created on Nov 27, 2014

@author: justin
'''
import sys, pygame
import math

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
clock = pygame.time.Clock()
plotPoints = [];
angle = 0
a = 5
lineCoord = x, y = 80 + math.cos(angle) * 50, 240 + math.sin(angle) * 50

def drawCircle():
    screen.fill([255, 255, 255])
    pygame.draw.circle(screen, [0, 0, 0], [80, 240], 50, 1)
    pygame.draw.circle(screen, [0, 0, 0], [80, 240], 3, 0)
    pygame.draw.aaline(screen, [0, 0, 0], [80, 240], lineCoord, 1)
    pygame.draw.line(screen, [0, 0, 0], [80, 0], [80, 480], 1)
    pygame.draw.line(screen, [0, 0, 0], [0, 240], [640, 240], 1)
    pygame.draw.line(screen, [0, 255, 255], [x, y], plotPoints[len(plotPoints) - 1], 1)

def shiftWave(plotPoints):
    for point in plotPoints:
        if point[0] > 640:
            plotPoints.remove(point)
        else:
            point[0] += a

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
    angle += 0.1
    if angle > (math.pi * 2):
        angle = angle - (math.pi * 2)
    lineCoord = x, y = 80 + math.cos(angle) * 50, 240 + math.sin(angle) * 50 
    shiftWave(plotPoints)
    plotPoints.append([x, y])
    drawCircle()
    if len(plotPoints) > 1:
        pygame.draw.lines(screen, [219, 7, 31], False, plotPoints, 1)
    pygame.display.flip()
    clock.tick(10)