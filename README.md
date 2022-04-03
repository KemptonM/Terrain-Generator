# Terrain-Generator
Final project for intro to programming (COS 125).
Check out the screenshots folder for some examples.

`maillett_terrain.py` was provided by my professor (with some of my modifications made). It generates two parallel matricies, one with different elevation values and the other with color assignments based on height. Originally, a pre-defined color value would be assigned to a cell, based which range its elevation value lies in. I modifed this so that it would assign an RGB value instead, still based on its elevation value. Since tkinter can't read RGB values, I used a small helper function for conversion.

![alt text](https://github.com/KemptonM/Terrain-Generator/blob/main/screenshots/Green%202.pngimage.jpg?raw=true)
