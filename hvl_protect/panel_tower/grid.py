import pygame
import random
from inventory.item.enemies import Enemy 
from inventory.item.towers import Tower
from inventory.item.towers import TowerSelector

class Grid:
    def __init__(self, screen, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "green"
        self.width = screen.get_width()
        self.height = int(screen.get_height()*(2/3))
        self.num_rows = 5
        self.num_columns = 10
        self.grid_size = 30
        self.selected_grid = [-1, -1]
        # states: void, selected, placed
        self.mouse_state = "void"
        self.enemies = []

        self.selector = TowerSelector()
        self.towers = []
    
    def generater_selector_towers(self):
        tower_index = 0
        # For towers in the selector
        for tower in self.selector.towers:
            pygame.draw.rect(self.screen, self.selector.towers[tower_index].color, tower.shape)
            tower_index += 1
        tower_index = 0
        # For towers in the actual grid
        for tower in self.towers:
            pygame.draw.rect(self.screen, self.selector.towers[tower_index].color, tower.shape)
            tower_index += 1



    def select_tower(self,mouse_clicked_pos):
        for i in range(self.selector.n_of_towers):
            if (mouse_clicked_pos[0] >= self.selector.towers[i].shape[0] 
                and mouse_clicked_pos[0] <= self.selector.towers[i].shape[0]+self.selector.tower_selection_box_size
                and mouse_clicked_pos[1] >= self.selector.towers[i].shape[1] 
                and mouse_clicked_pos[1] <= self.selector.towers[i].shape[1]+self.selector.tower_selection_box_size):
                if self.selector.selected_tower_index == i: # deselect tower
                    self.selector.selected_tower_index = -1
                    self.selector.towers[i].color = self.selector.default_color
                else:
                    self.selector.selected_tower_index = i
                    self.selector.towers[i].color = self.selector.selected_color
                    self.placed_tower_flag = False # no tower has been placed

    def place_tower(self,pos):
        spawn_tower = Tower(corner_position=pos)
        self.towers.append(spawn_tower)
        self.selector.towers[self.selector.selected_tower_index].color = self.selector.default_color
        self.selector.selected_tower_index = -1
        

    def get_pixel_position(self, row, column):
        return (self.base[0] + self.width/self.num_columns/2 + column*self.width/self.num_columns, self.base[1] + self.height/self.num_rows/2 + row*self.height/self.num_rows)

    def draw_grid(self):
        for i in range(self.num_rows-1):
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
       

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1],self.width, self.height))
        self.draw_grid()    
        self.draw_enemies()    
        self.draw_grid()        
        self.generater_selector_towers()

        
   