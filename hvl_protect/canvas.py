# Example file showing a basic pygame "game loop"
import pygame
from panel_tower.grid import Grid as TowerGrid
from panel_question.grid import Grid as QuestionGrid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

panel_tower = TowerGrid(screen, base=[0,0])
panel_question = QuestionGrid(screen, base=[0,720*(2/3)])

dt = 0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_clicked_pos = pygame.mouse.get_pos()
            panel_tower.select_tower(mouse_clicked_pos)

            if panel_tower.mouse_state == "selected":
                if mouse_clicked_pos[1] <= 390: #TODO: assign variable
                    for i in range(panel_tower.num_columns):
                        for j in range(panel_tower.num_rows):
                            grid = panel_tower.get_pixel_position(i,j)
                            if(grid[0]-mouse_clicked_pos[0] >= 0):
                                break
                        if(grid[1]-mouse_clicked_pos[1] >= 0):
                            break
                    panel_tower.selected_grid = [i,j]
                    panel_tower.place_tower(pos=panel_tower.get_pixel_position(panel_tower.selected_grid[0], 
                                                                               panel_tower.selected_grid[1]))
                    panel_tower.mouse_state = "void"
            
            if panel_tower.selector.selected_tower_index == -1:
                panel_tower.mouse_state = "void"
            else:
                panel_tower.mouse_state = "selected"
            print(panel_tower.mouse_state)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("seashell4")

    panel_tower.update()
    panel_question.update()

    # if q pressed, quit
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
        # display closing message and close the game
        pygame.draw.rect(screen, "seashell4", pygame.Rect(0,0,screen.get_width(),screen.get_height()))
        pygame.font.init()
        myfont = pygame.font.SysFont('Arial', 30)
        text_surface = myfont.render('Closing...', False, (255, 255, 255))
        screen.blit(text_surface, (int(screen.get_width()/2)-64,int(screen.get_height()/2)-24))

        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()