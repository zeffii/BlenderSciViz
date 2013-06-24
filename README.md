BlenderSciViz
=============

Preliminary code for plotting data in Blender.

###What this project hopes to achieve?  
Create analogues for common plotting needs in the scientific and data community. Provide sufficiently readable 
examples as a foundation for maximum customization by those willing to learn.

###Useful code snippets and addons

These are tagged depending on if they are visible in a render or only in the 3d viewport. Where it makes sense, examples of both are given.

**Scatter plots**
- 1d array to point cloud, takes array of (x,y,z) tuples and generates vertices (non render)
- 1d array to point cloud, takes array of (x,y,z,c) tuples and generates colored dots (renderable)
 
**Line plots**
- [1d array to polyline](https://github.com/zeffii/BlenderSciViz/blob/master/intro_script.py), takes array of (x,y,z) tuples and generates, edge based mesh (non render)

**3D surface plot**
- 2d array to 3D mesh, takes n*n array of (x,y,z) tuples and generates a mesh (renderable)
- Automatic colour map for 3d mesh data (renderable)

###Todo

    plt.{x,y,z}label,   
    plt.gca, 
    plt.plot(cos(x in range(0,2*pi, 0.01*pi)) ),
