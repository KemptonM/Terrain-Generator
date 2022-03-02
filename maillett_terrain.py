# maillett_terrain.py
#  *mostly not my code, this file was provided by professor.
#  changed some lines to allow for an RGB gradient
# instead of a gray one. Modifications can be made to the RGB values
# for different colors.

import tkinter as tk
import random

def d2TerrainGen(terrain, tl, br, noise):
    if br[0]-tl[0]<=1 and br[1]-tl[1]<=1:
        return
    elif br[0]-tl[0]<=1 and br[1]-tl[1] > 1: # Y only
        mid_y = (tl[1]+br[1])//2
        mid_x = tl[0]

        if terrain[tl[0]][mid_y]==0:
            val = (
                terrain[tl[0]][tl[1]] +
                terrain[tl[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
        
            terrain[tl[0]][mid_y] = val

        if terrain[br[0]][mid_y] == 0:
            val = (
                terrain[br[0]][tl[1]] + 
                terrain[br[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[br[0]][mid_y] = val

        val = (
            terrain[tl[0]][tl[1]] +
            terrain[tl[0]][br[1]] +
            terrain[br[0]][tl[1]] +
            terrain[br[0]][br[1]]
        ) / 4 + random.uniform(-noise/2,noise/2)
        terrain[mid_x][mid_y] = val

        # Recursive calls
        d2TerrainGen(terrain, tl, (mid_x,mid_y), noise/2)
        d2TerrainGen(terrain, (mid_x,mid_y), br, noise/2)

    elif br[0]-tl[0] > 1 and br[1]-tl[1]<=1: # x only
        mid_x = (tl[0]+br[0])//2
        mid_y = tl[1]

        if terrain[mid_x][tl[1]] == 0:
            val = (
                terrain[tl[0]][tl[1]] +
                terrain[br[0]][tl[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[mid_x][tl[1]] = val

        if terrain[mid_x][br[1]] == 0:
            val = (
                terrain[tl[0]][br[1]] +
                terrain[br[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[mid_x][br[1]] = val

        val = (
            terrain[tl[0]][tl[1]] +
            terrain[tl[0]][br[1]] +
            terrain[br[0]][tl[1]] +
            terrain[br[0]][br[1]]
        ) / 4 + random.uniform(-noise/2,noise/2)
        terrain[mid_x][mid_y] = val

        # Recursive calls
        d2TerrainGen(terrain, tl, (mid_x,mid_y), noise/2)
        d2TerrainGen(terrain, (mid_x,mid_y), br, noise/2)
    else: # 4 case
        mid_x = (tl[0]+br[0])//2
        mid_y = (tl[1]+br[1])//2
        
        if terrain[tl[0]][mid_y]==0:
            val = (
                terrain[tl[0]][tl[1]] +
                terrain[tl[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
        
            terrain[tl[0]][mid_y] = val

        if terrain[br[0]][mid_y] == 0:
            val = (
                terrain[br[0]][tl[1]] + 
                terrain[br[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[br[0]][mid_y] = val

        if terrain[mid_x][tl[1]] == 0:
            val = (
                terrain[tl[0]][tl[1]] +
                terrain[br[0]][tl[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[mid_x][tl[1]] = val

        if terrain[mid_x][br[1]] == 0:
            val = (
                terrain[tl[0]][br[1]] +
                terrain[br[0]][br[1]]
            ) / 2 + random.uniform(-noise/2,noise/2)
            terrain[mid_x][br[1]] = val

        val = (
            terrain[tl[0]][tl[1]] +
            terrain[tl[0]][br[1]] +
            terrain[br[0]][tl[1]] +
            terrain[br[0]][br[1]]
        ) / 4 + random.uniform(-noise/2,noise/2)
        terrain[mid_x][mid_y] = val

        # Recursive calls
        d2TerrainGen(terrain, tl, (mid_x,mid_y), noise/2)
        d2TerrainGen(terrain, (mid_x, tl[1]), (br[0], mid_y), noise/2)
        d2TerrainGen(terrain, (tl[0], mid_y), (mid_x, br[1]), noise/2)
        d2TerrainGen(terrain, (mid_x, mid_y), br, noise/2)

def GetElevationMap(map_size, seed=None):

    random.seed(seed)

    # Ma constants
    noise = 1024.0
    size=map_size
    terrain = []
    for i in range(size):
        inner = []
        for j in range(size):
            inner.append(0.0)
        terrain.append(inner)

    # Init corners with random vals
    terrain[0][0] = random.uniform(-noise,noise)
    terrain[0][size-1] = random.uniform(-noise,noise)
    terrain[size-1][0] = random.uniform(-noise,noise)
    terrain[size-1][size-1] = random.uniform(-noise,noise)

    # RUN & PLOT
    d2TerrainGen(terrain, (0,0), (size-1,size-1), noise)


    max_val = -100000
    min_val = 100000
    for x in terrain:
        for y in x:
            if y > max_val:
                max_val = y
            elif y < min_val:
                min_val = y
            
    min_val = abs(min_val)
    max_val += min_val

    # Squash values to (0,1)
    for x in range(len(terrain)):
        for y in range(len(terrain[x])):
            terrain[x][y] = (terrain[x][y]+min_val) / (max_val)

    # Set the random seed back to None.
    random.seed(None)
    return terrain

def from_rgb(rgb):  # translates rgb so that tkinter can accept
    rgb = tuple(rgb)
    return "#%02x%02x%02x" % rgb        # I found this on stackoverflow: https://tinyurl.com/z475z7t4

def DisplayTerrainWithOverlays(elevation_map, *args):

    if len(args)%2 != 0:
        print("For every overlay, you must provide a color.")

    scale = 8
    size = len(elevation_map)
    colors = []
    rgb = [0, 0, 0]
    for i in range(1,99,1):
        colors.append(from_rgb(rgb))
        rgb[1] += 2

    root = tk.Tk()
    frame=tk.Frame(root, width=1000, height=1000)
    canvas = tk.Canvas(
        frame,
        bg='white', 
        height=1000, 
        width=1000,
        scrollregion=(0,0,size*scale,size*scale)
    )
    
    xsbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
    ysbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    xsbar.config(command=canvas.xview)
    ysbar.config(command=canvas.yview)

    canvas.config(xscrollcommand=xsbar.set,yscrollcommand=ysbar.set)

    for x in range(len(elevation_map)):
        for y in range(len(elevation_map[x])):
            _x = x*scale
            _y = y*scale
            try:
                if int(elevation_map[x][y]*(len(colors)-1)) < 0:
                    print(elevation_map[x][y])
                c = colors[int(elevation_map[x][y]*(len(colors)-1))]
                canvas.create_rectangle(_x,_y,_x+scale,_y+scale,fill=c)
            except IndexError:
                print(elevation_map[x][y]*len(colors))


    for i in range(0,len(args),2):
        for x in range(len(args[i])):
            for y in range(len(args[i][x])):
                _x = x*scale
                _y = y*scale
                if args[i][x][y]==1:
                    canvas.create_rectangle(_x,_y,_x+scale,_y+scale,fill=args[i+1])


    frame.pack(expand=True, fill=tk.BOTH)
    
    xsbar.pack(side=tk.BOTTOM, fill=tk.X)
    ysbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    root.mainloop()



def GenerateEmptyOverlay(map_size):
    overlay = []
    for i in range(map_size):
        inner = []
        for j in range(map_size):
            inner.append(0)
        overlay.append(inner)
    return overlay
