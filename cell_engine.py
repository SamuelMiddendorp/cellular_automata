import pygame
import random
import json
import time
from cell import *
from copy import deepcopy
class CellEngine():
    def __init__(self, display, cell_size: int, res: tuple):
        self.cell_size = cell_size
        self.py_display = display
        self.res_x = res[0]
        self.res_y = res[1]
        self.world = []
        self.max_x = int(self.res_x / cell_size)
        self.max_y = int(self.res_y / cell_size)
        self.init()
    def get_cell(self, x, y) -> Cell:
        _x = self.max_x - 1
        _y = self.max_y - 1
        if(x < 0 or y < 0 or x > _x or y > _y):
            return 1
        else:
            return self.world[y][x].type  
    def init(self):
        for i in range(self.max_y):
            colls = []
            for j in range(self.max_x):
                    colls.append(Cell(0))
            self.world.append(colls)
    def spawn_particle(self, x,y, particle_type: int):
        self.world[y][x].type = particle_type
    # def draw(self, color):
    #     t1 = time.time()
    #     cell_s = deepcopy(self.cell_size)
    #     for y in range(self.max_y):
    #         for x in range(self.max_x):
    #             if(self.world[y][x] == 2):
    #                 pygame.draw.rect(self.py_display, color, (x * cell_s, y * cell_s, cell_s, cell_s))
    #             if(self.world[y][x] == 1):
    #                 pygame.draw.rect(self.py_display, (140, 100, 100), (x * cell_s, y * cell_s, cell_s, cell_s))
    def draw(self, color):
        for y in range(self.max_y):
            for x in range(self.max_x):
                if(self.world[y][x].type == 2):
                    rect = (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.py_display, color, rect)
                if(self.world[y][x].type == 1):
                    rect = (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.py_display, (140, 100, 100), rect)

    def set_state(self, file: str):
        with open(file, "r") as f:
            self.world = json.load(f)
    def get_cell_state(self, x, y):
        return self.world[y][x]
    def reset_cell_updates(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                self.world[y][x].has_updated = False;
    def reset(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                self.world[y][x].type == 0
    def save_state_to_file(self):
        with open("state.json", "w") as f:
            json.dump(self.world, f)
    def take_step(self):
        self.reset_cell_updates()
        # updated_cells = []
        # - 1, -1 , - 1
        for y in range(self.max_y):
            for x in range(self.max_x):
                if(self.world[y][x].type == 2 and not self.world[y][x].has_updated):
                    if(self.get_cell(x,y+1) == 0):
                        self.world[y+1][x].type = 2
                        self.world[y+1][x].has_updated = True
                        self.world[y][x].type = 0
                        self.world[y][x].has_updated = True
                    elif(self.get_cell(x-1, y+1) == 0):
                        self.world[y+1][x-1].type = 2
                        self.world[y+1][x-1].has_updated = True
                        self.world[y][x].type = 0
                        self.world[y][x].has_updated = True
                    elif(self.get_cell(x+1, y+1) == 0):
                        self.world[y+1][x+1].type = 2
                        self.world[y+1][x+1].has_updated = True
                        self.world[y][x].type = 0
                        self.world[y][x].has_updated = True
                    elif(self.get_cell(x+1,y) == 0):
                        self.world[y][x+1].type = 2
                        self.world[y][x+1].has_updated = True
                        self.world[y][x].type = 0
                        self.world[y][x].has_updated = True
                    elif(self.get_cell(x-1,y) == 0):
                        self.world[y][x-1].type = 2
                        self.world[y][x-1].has_updated = True
                        self.world[y][x].type = 0
                        self.world[y][x].has_updated = True



                    

                    
                    
