import pygame

class Shapes:

    def __init__(self, surface):
        self.mainsurface = surface

    def draw_rectangle(self):
        pygame.draw.rect(self.mainsurface, (255, 0, 0), (350, 200, 125, 50))


    def draw_circle(self):
        pygame.draw.circle(self.mainsurface, (0, 0, 204), (300, 200), 100)

    def draw_ellipse(self):
        pygame.draw.ellipse(self.mainsurface, (255, 0, 0), (350, 400, 100, 175), width=2)
    def draw_z(self):
        pygame.draw.line(self.mainsurface, (102, 0, 204), (50, 50), (250, 50), width=10)
        pygame.draw.line(self.mainsurface, (102, 0, 204), (250, 50), (50, 200), width=5)
        pygame.draw.line(self.mainsurface, (102, 0, 204), (50, 200), (250, 200), width=10)

    def draw_pentagon(self):
        pygame.draw.polygon(self.mainsurface, (0, 255, 0), ((250, 0), (500, 200), (400, 500), (100, 500), (0, 200)
))