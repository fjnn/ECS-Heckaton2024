import pygame
import time
import random

class Shuttle:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.screen_color = "seashell4"
        self.score = 0

        self.body = [500, 500]
        self.speed = 60
        self.body_color = "red"
        self.body_size = 10
        
        self.enemies = [[50, 50]]
        self.enemy_size = 10
        self.enemy_color = "green"
        self.enemy_direction = "right"
        self.enemy_move_offset = 0

        self.bullets = []
        self.bullet_size = 2
        self.bullet_color = "white"

        self.enemy_bullets = []
        self.enemy_bullet_size = 2
        self.enemy_bullet_color = "purple"
        
        self.enemy_timer_max = 100
        self.enemy_timer_current = 0
        self.enemy_timer_random = random.randint(0, self.enemy_timer_max)
        self.start_time = time.time()


    def update(self):
        self.screen.fill(self.screen_color)
        pygame.draw.circle(self.screen, self.body_color, self.body, self.body_size)
        for enemy_pixel in self.enemies:
            pygame.draw.circle(self.screen, self.enemy_color, enemy_pixel, self.enemy_size)
        for bullet_pixel in self.bullets:
            pygame.draw.circle(self.screen, self.bullet_color, bullet_pixel, self.bullet_size)
        for bullet_pixel in self.enemy_bullets:
            pygame.draw.circle(self.screen, self.enemy_bullet_color, bullet_pixel, self.enemy_bullet_size)
            

    def get_window_size(self):
        return self.screen.get_width(), self.screen.get_height()
    
    def get_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            return "w"
        if keys[pygame.K_s]:
            return "s"
        if keys[pygame.K_a]:
            return "a"
        if keys[pygame.K_d]:
            return "d"
        if keys[pygame.K_SPACE]:
            return "space"
    def show_score(self, color="white", font="comic sans", size=20):
  
        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)
        
        # create the display surface object 
        # score_surface
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        
        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()
        
        # displaying text
        self.screen.blit(score_surface, score_rect)

    # game over function
    def game_over(self):
    
        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)
        
        # creating a text surface on which text 
        # will be drawn
        game_over_surface = my_font.render('Your Score is : ' + str(self.score), True, 'red')
        
        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()
        
        # setting position of the text
        game_over_rect.midtop = (self.screen.get_width()/2, self.screen.get_height()/4)
        
        # blit will draw the text on screen
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        
        # after 2 seconds we will quit the 
        # program
        time.sleep(2)
        
        # deactivating pygame library
        pygame.quit()
        
        # quit the program
        quit()
        
        
        