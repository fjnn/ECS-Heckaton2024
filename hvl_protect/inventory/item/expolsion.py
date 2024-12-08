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
