import pygame

class Tower:
    def __init__(self, corner_position=[0,0], size=30) -> None:
        self.health = 100
        self.position = corner_position
        self.size = size
        self.shape = pygame.Rect(corner_position[0],corner_position[1],size,size)
        self.color = "black"


class TowerSelector:
    def __init__(self) -> None:
        self.tower_selection_box_offset = [50, 400]
        self.tower_selection_box_size = 70
        self.space_between_tower_selection = 100
        self.tower_selection_box_color = "black"
        self.n_of_towers = 4
        self.towers = []
        self.generater_towers()
    
    def generater_towers(self):
        self.towers=[]
        for tower_index in range(self.n_of_towers):
            tower = Tower(size=self.tower_selection_box_size)
            tower.position[0] = self.tower_selection_box_offset[0] + tower_index*self.space_between_tower_selection
            tower.position[1] = self.tower_selection_box_offset[1]
            tower.shape[0] = tower.position[0]
            tower.shape[1] = tower.position[1]
            tower.shape[2] = self.tower_selection_box_size
            tower.shape[3] = self.tower_selection_box_size
            self.towers.append(tower)
            print(tower_index)


    
