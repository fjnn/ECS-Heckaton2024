import pygame

class Tower:
    def __init__(self, corner_position=[0,0], size=30, color="black") -> None:
        self.health = 100
        self.position = corner_position
        self.size = size
        self.shape = pygame.Rect(corner_position[0],corner_position[1],size,size)
        self.color = color

    def change_color(self, color):
        self.color = color


class TowerSelector:
    def __init__(self) -> None:
        self.tower_selection_box_offset = [50, 400]
        self.tower_selection_box_size = 70
        self.space_between_tower_selection = 100
        self.n_of_towers = 4
        self.towers = []
        self.tower_colors = self.n_of_towers*["black"]
        self.change_color_selected(index=-1)
        self.generater_towers()
    
    def generater_towers(self):
        self.towers=[]
        print(self.tower_colors)
        for tower_index in range(self.n_of_towers):
            tower = Tower(size=self.tower_selection_box_size, color=self.tower_colors[tower_index])
            tower.position[0] = self.tower_selection_box_offset[0] + tower_index*self.space_between_tower_selection
            tower.position[1] = self.tower_selection_box_offset[1]
            tower.shape[0] = tower.position[0]
            tower.shape[1] = tower.position[1]
            tower.shape[2] = self.tower_selection_box_size
            tower.shape[3] = self.tower_selection_box_size
            self.towers.append(tower)
    
    def change_color_selected(self, index):
        if not index == -1:
            self.tower_colors[index] = "blue"
            


    
