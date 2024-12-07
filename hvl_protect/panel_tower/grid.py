import pygame
import numpy as np

class Grid:
    def __init__(self, screen, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "green"
        self.width = screen.get_width()
        self.height = int(screen.get_height()*(2/3))
        self.num_rows = 5
        self.num_columns = 10
        self.tower_selection_box_offset = [50, 400]
        self.tower_selection_box_size = 70
        self.space_between_tower_selection = 100
        self.tower_selection_box_color = "black"
        self.n_of_towers = 4
        self.towers= 4*[pygame.Rect(0,0,0,0)]
    
    def generater_towers(self):
        tower_index = 0
        print("here")
        for tower in self.towers:
            tower[0] = self.tower_selection_box_offset[0] + tower_index*self.space_between_tower_selection
            tower[1] = self.tower_selection_box_offset[1]
            tower[2] = self.tower_selection_box_size
            tower[3] = self.tower_selection_box_size
            tower_index += 1
            print(tower[0], tower[1], tower[2], tower[3])
            pygame.draw.rect(self.screen, "black", tower)
        

    def get_pixel_position(self, row, column):
        return (self.base[0] + self.width/self.num_columns/2 + column*self.width/self.num_columns, self.base[1] + self.height/self.num_rows/2 + row*self.height/self.num_rows)

    def draw_grid(self):
        for i in range(self.num_rows-1):
            for j in range(self.num_columns):
                pygame.draw.circle(self.screen, "orange", self.get_pixel_position(i, j), 5)

        

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1],self.width, self.height))
        self.draw_grid()        
        self.generater_towers()

        

