import pygame
import random
from inventory.item.enemies import Enemy 

from inventory.item.energy import Energy
from util import write_text

class Grid:
    def __init__(self, screen, energy_manager: Energy, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "green"
        self.width = screen.get_width()
        self.height = int(screen.get_height()*(2/3))
        self.num_rows = 5
        self.num_columns = 10
        self.enemies = []
        self.energy_manager = energy_manager

    def get_pixel_position(self, row, column):
        return (self.base[0] + self.width/self.num_columns/2 + column*self.width/self.num_columns, self.base[1] + self.height/self.num_rows/2 + row*self.height/self.num_rows)

    def draw_grid(self):
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                pygame.draw.circle(self.screen, "orange", self.get_pixel_position(i, j), 5)


    def draw_enemies(self):
        # check if any enemies have to be removed
        for enemy in self.enemies:
            if enemy.position[0] < self.base[0] or enemy.health <= 0:
                self.enemies.remove(enemy)

        # after random time add a new enemy
        if pygame.time.get_ticks() % 60 == 0:

            row = random.randint(0, self.num_rows-2)
            enemy_position = self.get_pixel_position(row, self.num_columns-1)
            enemy = Enemy(enemy_position)
            self.enemies.append(enemy)
        
        # draw all enemies' updated positions
        for enemy in self.enemies:
            enemy.move()
            pygame.draw.circle(self.screen, enemy.color, (enemy.position[0], enemy.position[1]), enemy.size)
       
    def update_energy_bar(self):
        bar_height = 20
        text_size = 40
        ratio = self.energy_manager.current_energy / self.energy_manager.max_energy
        
        x_base, y_base = self.get_pixel_position(4, 4)
        x_end, y_end = self.get_pixel_position(4, 7)
        pygame.draw.rect(self.screen, "black", pygame.Rect(x_base, y_base-bar_height, x_end-x_base, bar_height*2))
        pygame.draw.rect(self.screen, "blue", pygame.Rect(x_base, y_base-bar_height/2, (x_end-x_base)*ratio, bar_height))
        write_text(self.screen, f"{self.energy_manager.current_energy}", x=x_base+(x_end-x_base)/2, y=y_base, size=text_size)


    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1],self.width, self.height))
        self.draw_grid()    
        self.draw_enemies()    
        self.update_energy_bar()

        
   