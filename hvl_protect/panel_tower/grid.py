import pygame
import random
from inventory.item.enemies import Enemy 
from inventory.item.expolsion import Explosion
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

        self.projectiles = []
        self.explosions = []

        self.show_grid = False


        self.selector = TowerSelector()
        self.towers = []

    
    def generater_towers(self):
        tower_index = 0
        # For towers in the selector
        for tower in self.selector.towers:
            pygame.draw.rect(self.screen, "grey", tower.shape)
            # reduce shape by 4 pixels around the borders
            reduced_shape = (tower.shape[0]+4, tower.shape[1]+4, tower.shape[2]-8, tower.shape[3]-8)
            pygame.draw.rect(self.screen, "lightblue4", reduced_shape)
            self.screen.blit(self.selector.tower_assets[tower_index], (tower.shape[0]+10, tower.shape[1]+10, tower.shape[2]-14, tower.shape[3]-14))
            tower_index += 1
        tower_index = 0
        # For towers in the actual grid
        for tower in self.towers:
            self.screen.blit(self.selector.tower_assets[tower_index%4],  (tower.shape[0]-4, tower.shape[1]-4, tower.shape[2]-8, tower.shape[3]-8))

            tower_index += 1
            pygame.draw.rect(self.screen, "black", tower)

    def select_tower(self,mouse_clicked_pos):
        for i in range(self.selector.n_of_towers):
            if (mouse_clicked_pos[0] >= self.selector.towers[i].shape[0] 
                and mouse_clicked_pos[0] <= self.selector.towers[i].shape[0]+self.selector.tower_selection_box_size
                and mouse_clicked_pos[1] >= self.selector.towers[i].shape[1] 
                and mouse_clicked_pos[1] <= self.selector.towers[i].shape[1]+self.selector.tower_selection_box_size):
                if self.selector.selected_tower_index == i: # deselect tower
                    self.selector.selected_tower_index = -1
                    self.selector.towers[i].color = self.selector.default_color
                    self.show_grid = False
                else:
                    self.selector.selected_tower_index = i
                    self.selector.towers[i].color = self.selector.selected_color
                    self.placed_tower_flag = False # no tower has been placed
                    self.show_grid = True

    def place_tower(self,pos):
        spawn_tower = Tower(corner_position=pos)
        self.towers.append(spawn_tower)
        self.energy_manager.current_energy -= spawn_tower.cost
        self.selector.towers[self.selector.selected_tower_index].color = self.selector.default_color
        self.selector.selected_tower_index = -1
        self.show_grid = False


    def get_pixel_position(self, row, column):
        return (self.base[0] + self.width/self.num_columns/2 + column*self.width/self.num_columns, self.base[1] + self.height/self.num_rows/2 + row*self.height/self.num_rows)

    def get_closest_grid_position(self, x, y):
        row = 0
        column = 0
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                if x > self.get_pixel_position(i,j)[0] and x < self.get_pixel_position(i+1,j+1)[0]:
                    column = j
                if y > self.get_pixel_position(i,j)[1] and y < self.get_pixel_position(i+1,j+1)[1]:
                    row = i
        return row, column

    def draw_grid(self):
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                pygame.draw.circle(self.screen, "lightsteelblue", self.get_pixel_position(i, j), 5)


    def draw_enemies(self):
        # check if any enemies have to be removed
        for enemy in self.enemies:
            if enemy.position[0] < self.base[0] or enemy.health <= 0:
                # self.collision_positions.append(enemy.position)
                self.explosions.append(Explosion(enemy.position))
                self.enemies.remove(enemy)
                self.current_score += 10

        # after random time add a new enemy
        if pygame.time.get_ticks() % 120 == 0:

            row = random.randint(0, self.num_rows-2)
            enemy_position = self.get_pixel_position(row, self.num_columns-1)
            enemy = Enemy(enemy_position)
            self.enemies.append(enemy)
        
        # draw all enemies' updated positions
        for enemy in self.enemies:
            enemy.move()
            enemy.swap_index()
            self.screen.blit(enemy.imgs[enemy.img_index], (enemy.position[0], enemy.position[1]))

    def tower_shots(self):
        laser_height = 10
        laser_width = 20
        if pygame.time.get_ticks() % 60 == 0:
            for i in range(self.n_of_towers):
                x, y = self.get_pixel_position(i, 0)
                y -= laser_height/2
                self.projectiles.append((x, y))

        for i, projectile in enumerate(self.projectiles):
            self.projectiles[i] = (projectile[0]+5, projectile[1])
            pygame.draw.rect(self.screen, "red", (self.projectiles[i][0], self.projectiles[i][1], laser_width, laser_height))

    def check_laser_hit(self):
        if len(self.projectiles) == 0 or len(self.enemies) == 0:
            return
        for projectile in self.projectiles:
            # print(f"projeciles position: {projectile}")
            if projectile[0] > self.screen.get_width():
                # print("projectile off screen")
                self.projectiles.remove(projectile)
                continue
            for enemy in self.enemies:
                enemy_row = self.get_closest_grid_position(enemy.position[0], enemy.position[1])[0]
                projectile_row = self.get_closest_grid_position(projectile[0], projectile[1])[0]
                if enemy_row == projectile_row and projectile[0]+20 > enemy.position[0]:
                    enemy.take_damage(25)
                    try:
                        self.projectiles.remove(projectile)
                    except:
                        continue
    
    def draw_explosion(self):
        for explosion in self.explosions:
            explosion_img = explosion.update_explosion()
            if explosion_img is None:
                self.explosions.remove(explosion)
                continue
            self.screen.blit(explosion_img, explosion.position)


       
    def update_energy_bar(self):
        bar_height = 20
        text_size = 40
        ratio = self.energy_manager.current_energy / self.energy_manager.max_energy
        
        x_base, y_base = self.get_pixel_position(4, 4)
        x_end, y_end = self.get_pixel_position(4, 7)
        # pygame.draw.rect(self.screen, "black", pygame.Rect(x_base, y_base-bar_height, x_end-x_base, bar_height*2))
        pygame.draw.rect(self.screen, "grey", pygame.Rect(x_base-6, y_base-bar_height, x_end-x_base+6, bar_height*2))
        pygame.draw.rect(self.screen, "lightblue4", pygame.Rect(x_base, y_base-bar_height/2-4, (x_end-x_base)*ratio, bar_height+8))
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

        self.draw_enemies()
        if self.show_grid:
            self.draw_grid()        
        self.generater_selector_towers()
        self.update_energy_bar()      
        self.update_scoring()
        self.tower_shots()
        self.check_laser_hit()
        self.draw_explosion()

        
   