import pygame
from cell_engine import *
from pygame.locals import *
import sounddevice as sd
import numpy as np
# def print_sound(indata, outdata, frames, time, status):
#     volume_norm = np.linalg.norm(indata)*10
#     print ("|" * int(volume_norm))
# screen_res should be a multiple of 64 to facilitate large cell sizes if desired
screen_res = (1024, 768)
cell_size = 8
# fs = 44100
# sd.default.samplerate = fs
# sd.default.channels = 2
pygame.init()
display = pygame.display.set_mode(screen_res)
pygame.display.set_caption("Cellular Automata")
clock = pygame.time.Clock()
world = CellEngine(display, cell_size, screen_res)
# stream = sd.InputStream(callback=print_sound)# 
volume = 10
#np.linalg.norm(
# spawntimer = 0
isSpawning = False
fps = 60
particle = 2
while(True):
    
    # volume = np.linalg.norm(sd.rec(100,blocking=True))* 10
    # t1 = time.time()
    clock.tick(fps)
    event = pygame.event.poll()    # Look for any event
    if event.type == pygame.QUIT:  # Window close button clicked?
        break   
    if event.type == pygame.MOUSEBUTTONDOWN:
        isSpawning = True
    elif event.type == pygame.MOUSEBUTTONUP:
        isSpawning = False
    if event.type == pygame.KEYDOWN:
        if event.key == K_i:
            pos = pygame.mouse.get_pos()
            print(world.get_cell_state(int(pos[0] / cell_size), int(pos[1] / cell_size)))
        if event.key == K_1:
            fps = 5
        elif event.key == K_2:
            fps = 30
        elif event.key == K_3:
            fps = 60
        elif event.key == K_s:
            world.save_state_to_file()
        elif event.key == K_l:
            world.set_state("state.json")
        elif event.key == K_q:
            particle = 2
        elif event.key == K_w:
            particle = 1
        elif event.key == K_r:
            world.reset()
        elif event.key == K_d:
            particle = 0
                    

    if(isSpawning):
        pos = pygame.mouse.get_pos()
        world.spawn_particle(int(pos[0] / cell_size), int(pos[1] / cell_size), particle)
        # world.spawn_particle(5,0,2)
    world.take_step()
    display.fill((0,0,0))
    world.draw((235,167,83))
    pygame.display.flip()