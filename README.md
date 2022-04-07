# Terrain-Generator
Final project for intro to programming (COS 125).

`maillett_terrain.py` was provided by my professor (with some of my modifications made). It generates two parallel matricies, one with different elevation values and the other blank, each cell to be assigned a color value based on the height value of the first matrix.

My first implementations were "ocean cells", which all held a height lower than the specified ocean level. Next, I added a river function that would randomly select cells, turn them blue, and recursively do the same for the lowest adjacent cell. Originally, the color matrix would assign a range of pre-defined gray values to all cells that qualified as "land cells". 

![computer generated terrain map with grayscale terrain](https://github.com/KemptonM/Terrain-Generator/blob/main/screenshots/Earliest%20version.png)

I modifed this so that it would assign an RGB value instead, either a darker or lighter shade of green depending on the magnitude of the height value. Since tkinter can't read RGB values, I used a small helper function for conversion. This modifcation creates a nice grassy gradient, instead of a grayscale terrain.

![computer generated terrain map with large lake and green terrain](https://github.com/KemptonM/Terrain-Generator/blob/main/screenshots/Green%202.png)
![computer generated terrain map with lots of ocean and green terrain](https://github.com/KemptonM/Terrain-Generator/blob/main/screenshots/Green.png)
