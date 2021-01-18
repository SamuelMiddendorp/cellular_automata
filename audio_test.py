import time

res_y = 540
res_x = 960

cells = []
for y in range(res_y):
    colls = []
    for x in range(res_x):
        colls.append(x)
    cells.append(colls)
x = "hjel;l;"
t1 = time.time()
for y in range(res_y):
    for x in range(res_x):
        if(y % 2 == 0):
            cells[y][x] = y
        else:
            cells[y][x] = 0
t2 = time.time()

x = t2-t1

pass
        



