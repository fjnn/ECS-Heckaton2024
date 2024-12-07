# Example file showing a basic pygame "game loop"
import pygame
from inventory.item.enemies import Enemy 
from panel_tower.grid import Grid as TowerGrid
from panel_question.grid import Grid as QuestionGrid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
enemy_1 = Enemy() ## Can/Must be a list later on
enemy_2 = Enemy()
enemy_2.position = [400, 400]
enemies = [enemy_1, enemy_2]

panel_tower = TowerGrid(screen, base=[0,0])
panel_question = QuestionGrid(screen, base=[0,720*(2/3)])

dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("seashell4")


    for enemy in enemies:
        pygame.draw.circle(screen, enemy.color, enemy.position, enemy.size)

    panel_tower.update()
    panel_question.update()

    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()