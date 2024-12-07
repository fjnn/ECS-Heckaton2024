# Example file showing a basic pygame "game loop"
import pygame
from panel_tower.grid import Grid as TowerGrid
from panel_question.grid import Grid as QuestionGrid
from inventory.item.energy import Energy

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

energy_manager = Energy()

panel_tower = TowerGrid(screen, energy_manager=energy_manager, base=[0,0])
panel_question = QuestionGrid(screen, base=[0,screen.get_height()*(2/3)], energy_manager=energy_manager)

dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("seashell4")

    panel_tower.update()
    panel_question.update()

    # if q pressed, quit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
        # display closing message and close the game
        background_img = pygame.image.load("assets/background_space.png").convert_alpha()
        screen.blit(background_img, (0,0))
        pygame.font.init()
        myfont = pygame.font.SysFont('Arial', 30)
        text_surface = myfont.render('Closing...', False, (255, 255, 255))
        screen.blit(text_surface, (int(screen.get_width()/2)-64,int(screen.get_height()/2)-24))

        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()