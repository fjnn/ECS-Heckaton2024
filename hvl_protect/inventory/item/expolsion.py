import random
import pygame


class Explosion:
    def __init__(self, position) -> None:
        self.position = position
        self.imgs = []
        self.imgs.append(pygame.image.load("assets/explosion1.png").convert_alpha())
        self.imgs.append(pygame.image.load("assets/explosion2.png").convert_alpha())
        self.imgs.append(pygame.image.load("assets/explosion3.png").convert_alpha())
        self.img_index = 0
        self.swap_cntr = 0
        # self.generate()

    def update_explosion(self):
        """
        Update the explosion animation.
        """
        self.swap_cntr += 1
        if self.swap_cntr >= 10:
            self.img_index += 1
            self.swap_cntr = 0
        
        if self.img_index >= len(self.imgs):
            return None
        
        return self.imgs[self.img_index]

    #     # self.swap_index()

    # def swap_index(self):
    #     """
    #     Swap the image index to change the enemy's appearance.
    #     """
    #     self.swap_cntr += 1
    #     if self.swap_cntr >= 30/self.speed:
    #         self.img_index = 1 - self.img_index
    #         self.swap_cntr = 0

    # def move(self):
    #     """
    #     Move the enemy towards the base with its speed.
    #     Movement is horizontal only.
    #     """

    #     self.position = (self.position[0] - self.speed, self.position[1])