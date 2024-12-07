import pygame

class Grid:
    def __init__(self, screen, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "green"
        self.width = 500

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(30, 30, 60, 60))
        
