def take_step(self):
        updated_cells = []
        for y in range(self.max_y - 1, -1 , - 1):
            for x in range(self.max_x):
                if(self.world[y][x] == 2  and ("y%ix%i" % (y,x)) not in updated_cells):
                    if(self.get_cell(x,y+1) == 0):
                        self.world[y+1][x] = 2
                        self.world[y][x] = 0
                    elif(self.get_cell(x+1,y) == 0):
                        self.world[y][x+1] = 2
                        updated_cells.append("y%ix%i" % (y,x+1))
                        self.world[y][x] = 0
                    elif(self.get_cell(x-1,y) == 0):
                        self.world[y][x-1] = 2
                        self.world[y][x] = 0
def take_step(self):
    updated_cells = []
    for y in range(self.max_y - 1, -1 , - 1):
        for x in range(self.max_x):
            if(self.world[y][x] == 2 and not ("y%ix%i" % (y,x)) in updated_cells ):
                if(self.get_cell(x,y+1) == 0):
                    self.world[y+1][x] = 2
                    self.world[y][x] = 0
                # elif(self.get_cell(x-1, y+1) == 0 and self.get_cell(x-1,y) == 0):
                #     self.world[y+1][x-1] = 2
                #     updated_cells.append(self.world[y+1][x-1])
                #     self.world[y][x] = 0
                # elif(self.get_cell(x+1, y+1) == 0 and self.get_cell(x+1,y) == 0):
                #     self.world[y+1][x+1] = 2
                #     updated_cells.append(self.world[y+1][x+1])
                #     self.world[y][x] = 0
                elif(self.get_cell(x-1,y) == 0 and self.get_cell(x+1, y) != 0):
                    self.world[y][x-1] = 2
                    self.world[y][x] = 0
                elif(self.get_cell(x+1,y) == 0 and self.get_cell(x-1, y) != 0):
                    self.world[y][x+1] = 2
                    updated_cells.append("y%ix%i" % (y,x+1))
                    self.world[y][x] = 0
