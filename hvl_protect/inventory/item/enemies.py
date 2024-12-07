import random

class Enemy:
    def __init__(self, grid_width, grid_height) -> None:
        self.generate(grid_width, grid_height)

    def generate(self, grid_width, grid_height):
        """
        Generate a new enemy with random position and speed.
        """ 

        self.position = [random.randint(int(grid_width/2), grid_width), random.randint(0, grid_height)]
        self.color = "red"
        self.speed = random.randint(1, 10)
        self.size = 10

    def move(self):
        """
        Move the enemy towards the base with its speed.
        Movement is horizontal only.
        """

        self.position[0] -= self.speed
