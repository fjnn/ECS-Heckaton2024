import pygame
import random
from inventory.item.enemies import Enemy 
from inventory.item.towers import Tower
from inventory.item.towers import TowerSelector

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
        self.grid_size = 30
        self.selected_grid = [-1, -1]
        # states: void, selected, placed
        self.mouse_state = "void"
        self.enemies = []
        self.energy_manager = energy_manager
        self.background = pygame.image.load("assets/background_space.png").convert_alpha()
        self.tower_selection_box_offset = [50, 400]
        self.tower_selection_box_size = 70
        self.space_between_tower_selection = 100
        self.tower_selection_box_color = "black"
        self.n_of_towers = 4
        self.towers= 4*[pygame.Rect(0,0,0,0)]
        self.current_score = 0
        self.tower_assets = [
            pygame.image.load("assets/tower1.png").convert_alpha(),
            pygame.image.load("assets/tower2.png").convert_alpha(),
            pygame.image.load("assets/tower3.png").convert_alpha(),
            pygame.image.load("assets/tower1.png").convert_alpha()
        ]


        self.selector = TowerSelector()
        self.towers = []
    
    def generater_selector_towers(self):
        tower_index = 0
        # For towers in the selector
        for tower in self.selector.towers:
            self.screen.blit(self.tower_assets[tower_index], tower.shape)
            # pygame.draw.rect(self.screen, self.selector.towers[tower_index].color, tower.shape)
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
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                pygame.draw.circle(self.screen, "orange", self.get_pixel_position(i, j), 5)


    def draw_enemies(self):
        # check if any enemies have to be removed
        for enemy in self.enemies:
            if enemy.position[0] < self.base[0] or enemy.health <= 0:
                self.enemies.remove(enemy)
                self.current_score += 10

        # after random time add a new enemy
        if pygame.time.get_ticks() % 60 == 0:

            row = random.randint(0, self.num_rows-2)
            enemy_position = self.get_pixel_position(row, self.num_columns-1)
            enemy = Enemy(enemy_position)
            self.enemies.append(enemy)
        
        # draw all enemies' updated positions
        for enemy in self.enemies:
            enemy.move()
            enemy.swap_index()
            self.screen.blit(enemy.imgs[enemy.img_index], (enemy.position[0], enemy.position[1]))
            # pygame.draw.circle(self.screen, enemy.color, (enemy.position[0], enemy.position[1]), enemy.size)
       
    def update_energy_bar(self):
        bar_height = 20
        text_size = 40
        ratio = self.energy_manager.current_energy / self.energy_manager.max_energy
        
        x_base, y_base = self.get_pixel_position(4, 4)
        x_end, y_end = self.get_pixel_position(4, 7)
        pygame.draw.rect(self.screen, "black", pygame.Rect(x_base, y_base-bar_height, x_end-x_base, bar_height*2))
        pygame.draw.rect(self.screen, "blue", pygame.Rect(x_base, y_base-bar_height/2, (x_end-x_base)*ratio, bar_height))
        write_text(self.screen, f"{self.energy_manager.current_energy}", x=x_base+(x_end-x_base)/2, y=y_base, size=text_size)

    def update_scoring(self):
        text_size = 80
        x_start, y_start = self.get_pixel_position(4, 8)
        x_end, y_end = self.get_pixel_position(4, 9)
        write_text(self.screen, f"{self.current_score}", x=x_start+(x_end-x_start)/2, y=y_start, size=text_size)
        pass

    def update(self):
        # draw the background from the assets
        self.screen.blit(self.background, (self.base[0], self.base[1]))

        self.draw_grid()    
        self.draw_enemies()    
        self.draw_grid()        
        self.generater_selector_towers()
        self.update_energy_bar()      
        self.update_scoring()

        
   