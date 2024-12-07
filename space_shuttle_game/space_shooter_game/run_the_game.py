# Example file showing a basic pygame "game loop"
import pygame
from space_shuttle import Shuttle 
import game_play as game_play

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

shuttle = Shuttle(screen)
game_play.main_start(shuttle)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(shuttle.screen_color)

    game_play.main_update(shuttle)
    shuttle.show_score()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(shuttle.speed)  # limits FPS to 60

pygame.quit()