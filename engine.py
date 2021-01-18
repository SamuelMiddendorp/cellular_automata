import pygame
import random
from copy import deepcopy
local_world = []
max_x = 0
max_y = 0
def generate_world(cell_size: int, res_x: int, res_y:int) -> list:
    world = []
    x = int(res_x / cell_size)
    y = int(res_y / cell_size)
    max_x = x - 1
    max_y = y - 1
    for i in range(x):
        colls = []
        for j in range(y):
            if(i == 0 and (j <= 4)):
                colls.append("x")
            else:
                colls.append("")
        world.append(colls)
    local_world = world
    return world
def draw_world(screen, world: list, cell_size: int, color: tuple):
    for x, row in enumerate(world):
        for y, collum in enumerate(row):
            if(collum == "x"):
                pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
def get_cell(x, y):
    if(x < 0 or y < 0 or x > max_x or y > max_y):
        return "x"
    else:
        return local_world[x][y]
def take_step(world):
    temp_world = deepcopy(world)
    for x, row in enumerate(world):
        for y, collum in enumerate(row):
            if(collum == "x"):
                if(get_cell(x,y+1) == ""):
                    temp_world[x][y + 1] = "x"
                    temp_world[x][y] = ""
                    print("triggered")
                elif(world[x-1][y+1] == ""):
                    temp_world[x-1][y + 1] = "x"
                    temp_world[x][y] = ""
                    print("triggered left")
                elif(world[x+1][y+1] == ""):
                    temp_world[x+1][y+1] = "x"
                    temp_world[x][y] = ""
    local_world = temp_world
    return temp_world
    
