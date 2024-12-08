import pygame

class Tower:
    def __init__(self, corner_position=[0,0], size=30, color="yellow") -> None:
        self.health = 100
        self.size = size
        self.shape = pygame.Rect(corner_position[0]-int(size/2), corner_position[1]- int(size/2),size,size)
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
        self.generater_towers()
        self.change_color_selected(index=-1)
        self.selected_tower_index = None
        self.default_color = "yellow"
        self.selected_color = "blue"
    
    def generater_towers(self):
        self.towers=[]
        for _ in range(self.n_of_towers):
            tower = Tower()
            self.towers.append(tower)
    
        tower_index = 0
        for tower in self.towers:
            tower.shape[0] = self.tower_selection_box_offset[0] + tower_index*self.space_between_tower_selection
            tower.shape[1] = self.tower_selection_box_offset[1]
            tower.shape[2] = self.tower_selection_box_size
            tower.shape[3] = self.tower_selection_box_size
            tower_index += 1

    
    def change_color_selected(self, index):
        if not index == -1:
            self.towers[index].color = "blue"
            


    
