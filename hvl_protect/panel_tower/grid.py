import pygame
from inventory.item.enemies import Enemy 

class Grid:
    def __init__(self, screen, base=[0,0]) -> None:
        self.base = base
        self.screen = screen
        self.color = "green"
        self.width = screen.get_width()
        self.height = int(screen.get_height()*(2/3))
        self.num_rows = 5
        self.num_columns = 10
        self.enemies = [
            Enemy(self.base, self.width, self.height),
        ]

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
            enemy = Enemy(self.base, self.width, self.height)
            self.enemies.append(enemy)
        
        # draw all enemies' updated positions
        for enemy in self.enemies:
            enemy.move()
            pygame.draw.circle(self.screen, enemy.color, (enemy.position[0], enemy.position[1]), enemy.size)
       

    def update(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.base[0], self.base[1],self.width, self.height))
        self.draw_grid()    
        self.draw_enemies()    

        
   