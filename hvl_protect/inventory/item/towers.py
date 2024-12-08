import pygame

class Tower:
    def __init__(self, corner_position=[0,0], size=30, asset=None, cost=10) -> None:
        self.health = 100
        self.size = size
        self.shape = pygame.Rect(corner_position[0]-int(size/2), corner_position[1]- int(size/2),size,size)
        self.cost = cost 
        self.asset = asset
    
    def get_center_pos(self):
        row = self.shape[0]+self.size/2
        col = self.shape[1]+self.size/2
        return row, col



class TowerSelector:
    def __init__(self) -> None:
        self.tower_selection_box_offset = [50, 400]
        self.tower_selection_box_size = 70
        self.space_between_tower_selection = 100
        self.n_of_towers = 4
        self.towers = []
        self.selected_tower_index = None
        self.default_color = "yellow"
        self.selected_color = "blue"
        self.tower_assets = [
            pygame.image.load("assets/tower1.png").convert_alpha(),
            pygame.image.load("assets/tower2.png").convert_alpha(),
            pygame.image.load("assets/tower3.png").convert_alpha(),
            pygame.image.load("assets/tower1.png").convert_alpha()
        ]
        self.generater_towers()
    
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

            tower.asset = self.tower_assets[tower_index]
            tower_index += 1

            


    
