import pygame, sys
from pygame.locals import *
import shapes

pygame.init()
mainsurface = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Some Shapes")
mainsurface.fill((255, 255, 255))

draw = shapes.Shapes(mainsurface)
draw.draw_ellipse()
draw.draw_pentagon()
draw.draw_rectangle()
draw.draw_circle()
draw.draw_z()
pygame.display.update()  # necessary to start
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

