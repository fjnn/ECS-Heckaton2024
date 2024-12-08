import random
import pygame

ENEMY_SIZE = 10

class Enemy:
    def __init__(self, position) -> None:
        self.health = 100
        self.position = position
        # Set the size for the image
        DEFAULT_IMAGE_SIZE = (30, 30)
        
        # Scale the image to your needed size
        # image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        self.imgs = []
        self.imgs.append(pygame.image.load("assets/enemy1.png").convert_alpha())
        self.imgs.append(pygame.image.load("assets/enemy2.png").convert_alpha())
        self.imgs[0] = pygame.transform.scale(self.imgs[0], DEFAULT_IMAGE_SIZE)
        self.imgs[1] = pygame.transform.scale(self.imgs[1], DEFAULT_IMAGE_SIZE)

        self.explosion_imgs = []
        self.explosion_imgs.append(pygame.image.load("assets/explosion1.png").convert_alpha())
        self.explosion_imgs.append(pygame.image.load("assets/explosion2.png").convert_alpha())
        self.explosion_imgs.append(pygame.image.load("assets/explosion3.png").convert_alpha())
        self.explosion_position = (0, 0)
        self.explosion_cntr = 0
        # self.img_height = self.imgs[0].get_height()
        # self.position[1] = self.position[1]-self.img_height/2
        self.position = (self.position[0], self.position[1]-self.imgs[0].get_height()/2)
        self.img_index = 0
        self.swap_cntr = 0
        self.generate()

    def swap_index(self):
        """
        Swap the image index to change the enemy's appearance.
        """
        self.swap_cntr += 1
        if self.swap_cntr >= 30/self.speed:
            self.img_index = 1 - self.img_index
            self.swap_cntr = 0

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