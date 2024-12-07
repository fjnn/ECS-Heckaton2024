import pygame

class Grid:
    def __init__(self, screen, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "yellow"
        self.width = 1280
        self.height = 720*(1/3)

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1],self.width, self.height))
        
