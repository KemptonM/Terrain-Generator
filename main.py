# NAME: KEMPTON MAILLETT | COS125
# ASSIGNMENT: PROJECT 2
# COLLABORATION: NONE
# This program uses a given array and creates ocean, 
# river, and beach cells based on height values.

# potential overlays:
#   farmland around rivers
#   groups of houses
#       try to identify flatlands
#   beaches (done)
#   ponds

import random
import maillett_terrain as terrain

def genBodies(elevation, ocean, waterLevel):
    for r in range(len(elevation)):
        for c in range(len(elevation[r])):
            if elevation[r][c] <= waterLevel:   # if point is at or below water level
                ocean[r][c] = 1                   # water is true
            else:                               # else
                ocean[r][c] = 0                   # no water

def genRivers(elevation, overlay, waterLevel):
    # fill 50 spots with water, then send the water downstream
    # check for best spots:
    for x in range(50):
        x = random.randrange(0, len(elevation))
        y = random.randrange(0, len(elevation[0]))
        flow(elevation, overlay, waterLevel, x, y)
 
def flow(elevation, overlay, waterLevel, x, y):
    # Function to recursively flow water onto neighboring cells that flow downstream
    x_ = x      # x coordinate being checked
    y_ = y      # y coordinate being checked
    try:            # get the minimum
        for x2 in range(-1, 2):     # check 1 cell radius
            for y2 in range(-1,2):
                if elevation[x+x2][y+y2] < elevation[x_][y_]: 
                    x_ = x+x2       # save smallest
                    y_ = y+y2
        if elevation[x_][y_] <= waterLevel:
            # we've reached the ocean
            return
        elif overlay[x_][y_] == 1:
            return
        else:
            overlay[x][y] = 1
            flow(elevation, overlay, waterLevel, x_, y_)
    except IndexError: # kind of a hack, should fix index errors
        return

def genBeaches(elevation, beaches, waterLevel):
    # Generate beaches near waterlevel
        for r in range(len(elevation)):
            for c in range(len(elevation)):
                if elevation[r][c] <= waterLevel:
                    try:
                        for r2 in range(-1, 2):
                            for c2 in range(-1, 2):
                                if elevation[r+r2][c+c2] > waterLevel:
                                    sandSpread(elevation, beaches, waterLevel, r, c)
                    except IndexError:
                        continue

def sandSpread(elevation, beaches, waterLevel, r, c, count = 0):
    # Recursive function to spread sand to neighboring land cells
    try:
        for r2 in range(-1, 2):
            for c2 in range(-1, 2):
                if elevation[r+r2][c+c2] > waterLevel:      # if adjacent cell isn't water:
                    beaches[r+r2][c+c2] = 1                     # apply another beach cell
                    # print(f"genBeaches count: {count+1}") # uncomment to count number of beaches in console
                    if count < 2:   # do it twice
                        sandSpread(elevation, beaches, waterLevel,
                        r+r2, c+c2, count + 1)
                    else:
                        return
    except IndexError:
        return

def main():

    size = 125              # size of grid
    waterLevel = 0.4       # this can be changed
    elevation = terrain.GetElevationMap(size)       # get the elevation map
    ocean = terrain.GenerateEmptyOverlay(size)      # generate an empty ocean overlay
    rivers = terrain.GenerateEmptyOverlay(size)     # generate an empty river overlay
    beaches = terrain.GenerateEmptyOverlay(size)    # generate an empty beaches overlay

    genBodies(elevation, ocean, waterLevel)         # generate the ocean
    genBeaches(elevation, beaches, waterLevel)
    genRivers(elevation, rivers, waterLevel)        # generate the rivers

    terrain.DisplayTerrainWithOverlays (
        elevation,                          # pass in the elevation map
        ocean, 'midnight blue',             # display ocean, dark blue
        rivers, 'blue4',                    # display rivers, lighter blue
        beaches, 'khaki2'
    )

main()
