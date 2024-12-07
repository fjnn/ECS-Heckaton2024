import random

ENEMY_SIZE = 10

class Enemy:
    def __init__(self, position) -> None:
        self.health = 100
        self.position = position
        self.generate()

    def generate(self):
        """
        Generate a new enemy with random position and speed.

        """ 

        self.color = "red"
        self.speed = random.randint(1, 3)
        self.size = ENEMY_SIZE

    def move(self):
        """
        Move the enemy towards the base with its speed.
        Movement is horizontal only.
        """

        self.position = (self.position[0] - self.speed, self.position[1])

    
    def take_damage(self, damage):
        """
        Reduce the enemy's health by the damage amount.

        Args:
            damage (int): The amount of damage to deal.
        """

        self.health -= damage