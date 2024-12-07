import random
from space_shuttle import Shuttle
import time

def spawn_shuttle(shuttle:Shuttle):
    # STUDENTS
    # Define a list called shuttle.body. It will hold [x, y] pixels.
    # In the snake game, there were many pixels to define the body
    # Here we have only one. You don't need a nested list.
    pass

def spawn_enemy(shuttle:Shuttle):
    # STUDENTS
    # Define a list called shuttle.enemies. It will hold [x, y] pixels of the enemIES.
    # In the snake game, there were only one pixel to define the fruit
    # Here we several enemies. You need a nested list.
    pass

def change_color_and_size(shuttle:Shuttle):
    # STUDENTS
    # You can change the color and the size of the objects on the screen if you want.
    # https://www.pygame.org/docs/ref/color_list.html
    # color = (r,g,b)
    # use shuttle.X_color or shuttle.X_size
    # X can be body/enemy/bullet/screen/enemy_bullet
    pass      

def move_with_keys(shuttle:Shuttle):
    # STUDENTS
    # Make the “pixel” (a.k.a your shuttle) move as you press WASD keys.
    key = shuttle.get_key() 
    pass


def shoot(shuttle:Shuttle):
    # STUDENTS
    # Step-1: Fill the "shuttle.bullets" as you press "space" key.
    # Step-2: Remove the bullets from the list as they leave the screen.
    key = shuttle.get_key()  ## We need this here again because it was a LOCAL VARIABLE in the previous usage.


def move_enemies(shuttle:Shuttle):
    # STUDENTS (Chilli)
    # Here you are supposed to make the enemies move right and left.
    # you can use the variable "shuttle.enemy_move_offset" to keep the value of how much enemies moved from their initial location
    # You should define a max movement both to the right and left direction.
    # SUGGESTION: 
    #   You can first check which direction enemy moves (shuttle.enemy_direction)
    #   and make the pixels move accordingly in another if statement.
    pass
    

def hit_enemy(shuttle:Shuttle):
    # STUDENTS
    # The same principle as eating fruits in snake game
    # If the pixel of one of the shuttle.bullets is in vicinity pixel of one of the shuttle.enemies, remove that enemy from the shuttle.enemies list.
    pass

def enemy_shoot(shuttle:Shuttle):
    # One random enemy will shoot in every 5 seconds
    # You can get the current time with this command:
    current_time = time.time()

    # You can select a random enemy with this command:
    enemy = random.choice(shuttle.enemies)

    # Write the code for spawning a bullet (very similar to shoot() function but opposite direction) IF the elapsed time is 2 seconds (or more).

    # Additionally, you can print elapsed time in .2f seconds using f-strings
    
    pass




def game_over(shuttle:Shuttle):
    # STUDENTS
    # If a bullet hits you, then the game is over.
    
    # Call shuttle.game_over()

    pass



def main_start(shuttle):
    spawn_shuttle(shuttle)
    spawn_enemy(shuttle)
    change_color_and_size(shuttle)

def main_update(shuttle:Shuttle):
    move_with_keys(shuttle)
    move_enemies(shuttle)
    shoot(shuttle)
    hit_enemy(shuttle)
    enemy_shoot(shuttle)
    game_over(shuttle)

    shuttle.update()