# Terrain-Generator
Final project for intro to programming (COS 125).
Check out the screenshots folder for some examples.

`maillett_terrain.py` was provided by my professor (with some of my modifications made). It generates two parallel matricies, one with different elevation values and the other blank, each cell to be assigned a color value based on the height value of the first matrix.
Originally, the color matrix would assign `green` to all cells that had height values within within a specified range for "land". I modifed this so that it would assign an RGB value instead, either a darker or lighter shade of gray depending on the magnitude of the height value. Since tkinter can't read RGB values, I used a small helper function for conversion. This modifcation creates a nice grassy gradient, instead of a single-shade of green terrain.

![alt text](https://github.com/KemptonM/Terrain-Generator/blob/main/screenshots/Green%202.png)
