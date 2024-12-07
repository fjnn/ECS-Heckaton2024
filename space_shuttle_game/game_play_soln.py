import random
from space_shuttle import Shuttle
import time

def spawn_shuttle(shuttle:Shuttle):
    #STUDENTS
    shuttle.body = [650, 600]

def spawn_enemy(shuttle:Shuttle):
    #STUDENTS
    # shuttle.enemies = [[350, 50], [450, 50]]
    shuttle.enemies = [[350, 50], [450, 50], [550, 50], [650, 50], [400, 100], [500, 100], [600, 100]]

def change_color_and_size(shuttle:Shuttle):
    # https://www.pygame.org/docs/ref/color_list.html
    # color = (r,g,b)
    # use shuttle_X_color or shuttle_X_size
    # X can be body/enemy/bullet
    pass    

def move_with_keys(shuttle:Shuttle):
    # STUDENTS
    key = shuttle.get_key() 
    if key == "a":
        shuttle.body[0] -= 5
    elif key == "s":
        shuttle.body[1] += 5
    elif key == "d":
        shuttle.body[0] += 5
    elif key == "w":
        shuttle.body[1] -= 5
    else:
        # print("none")
        pass


def move_enemies(shuttle:Shuttle):
    move_max = 250
    move_min = -250
    if shuttle.enemy_move_offset <= move_max and shuttle.enemy_move_offset >= move_min:
        pass
    elif shuttle.enemy_move_offset < move_min:
        shuttle.enemy_direction = "right"

    elif shuttle.enemy_move_offset > move_max:
        shuttle.enemy_direction = "left"

    for pixel in shuttle.enemies:
        if shuttle.enemy_direction == "right":
            pixel[0] += 1
            shuttle.enemy_move_offset += 1
        else:
            pixel[0] -= 1
            shuttle.enemy_move_offset -= 1

def shoot(shuttle:Shuttle):
    key = shuttle.get_key()
    if key == "space":
        shuttle.bullets.append(shuttle.body.copy())
    # move bullets
    for bullet in shuttle.bullets:
        bullet[1] -= 3

    # remove bullets outside of the window
    for bullet in shuttle.bullets:
        if bullet[1] < 0:
            shuttle.bullets.remove(bullet)

    

def hit_enemy(shuttle:Shuttle):
    # STUDENTS
    for bullet in shuttle.bullets:
        for enemy in shuttle.enemies:
            if (abs(bullet[0]-enemy[0]) <=15 and abs(bullet[1]-enemy[1]) <=15):
                shuttle.enemies.remove(enemy)
                shuttle.score += 10

def enemy_shoot(shuttle:Shuttle):
    ## One random enemy will shot every 5 seconds
    # print elapsed time in .2f seconds
    current_time = time.time()
    elapsed_time = current_time - shuttle.start_time
    if elapsed_time >= 2.0:
        enemy = random.choice(shuttle.enemies)
        shuttle.enemy_bullets.append(enemy.copy())

        print(f"elapsed:{elapsed_time:.2f}")
        shuttle.start_time = current_time

    # move bullets
    for bullet in shuttle.enemy_bullets:
        bullet[1] += 3




def game_over(shuttle:Shuttle):
    width, height = shuttle.get_window_size()
    # STUDENTS
    for bullet in shuttle.enemy_bullets:
        if (abs(bullet[0]-shuttle.body[0]) <=15 and abs(bullet[1]-shuttle.body[1]) <=15):
            shuttle.game_over()



def main_start(shuttle):
    spawn_shuttle(shuttle)
    spawn_enemy(shuttle)
    change_color_and_size(shuttle)
    # spawn_fruit(snake)

def main_update(shuttle:Shuttle):
    move_with_keys(shuttle)
    move_enemies(shuttle)
    shoot(shuttle)
    hit_enemy(shuttle)
    enemy_shoot(shuttle)
    game_over(shuttle)

    shuttle.update()