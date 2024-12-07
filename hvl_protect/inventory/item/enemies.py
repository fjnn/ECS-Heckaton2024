import random

ENEMY_SIZE = 10

class Enemy:
    def __init__(self, grid_base, grid_width, grid_height) -> None:
        self.generate(grid_base, grid_width, grid_height)
        self.health = 100

    def generate(self, grid_base, grid_width, grid_height):
        """
        Generate a new enemy with random position and speed.

        Args:
            grid_base (list): The base of the grid as [x_offset, y_offset].
            grid_width (int): The width of the grid.
            grid_height (int): The height of the grid.
        """ 

        self.position = [
            random.randint(
                int(grid_width/2) + grid_base[0],
                grid_width - int(ENEMY_SIZE/2) + grid_base[0]  # offset the size to stay in bounds
            ), 
            random.randint(
                grid_base[1] + int(ENEMY_SIZE/2), 
                grid_height - int(ENEMY_SIZE/2) + grid_base[1]   # offset the size to stay in bounds
            )
        ]
        self.color = "red"
        self.speed = random.randint(1, 3)
        self.size = ENEMY_SIZE

    def move(self):
        """
        Move the enemy towards the base with its speed.
        Movement is horizontal only.
        """

        self.position[0] -= self.speed

    
    def take_damage(self, damage):
        """
        Reduce the enemy's health by the damage amount.

        Args:
            damage (int): The amount of damage to deal.
        """

        self.health -= damage