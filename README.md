BlenderSciViz
=============

Preliminary code for plotting data in Blender.

###What this project hopes to achieve?  
Create analogues for common plotting needs in the scientific and data community. Provide sufficiently readable 
examples as a foundation for maximum customization by those willing to learn.

###Useful code snippets

These are tagged depending on if they are visible in a render or only in the 3d viewport. Where it makes sense, examples of both are given.

**Scatter plots**
- [1d array to point cloud](https://github.com/zeffii/BlenderSciViz/blob/master/point_cloud_verts_only.py), takes array of `(x,y,z)` tuples and generates vertices (non render)
- [1d array to point cloud no color](https://github.com/zeffii/BlenderSciViz/blob/master/point_cloud_icospheres_only.py), takes array of `(x,y,z)` tuples and generates single color dots (small icospheres)(renderable)
- [1d array to point cloud with colors](https://github.com/zeffii/BlenderSciViz/blob/master/point_cloud_icospheres_colors.py), takes array of `((x,y,z),(r,g,b,a))` tuples and generates colored dots (renderable)
- [1d array to points in 3d grid (n*n*z height)](https://github.com/zeffii/BlenderSciViz/blob/master/point_cloud_3d_grid_from_1d_array.py), takes array of `(x,y,z)` tuples and generates vertices (non render)

**Line plots**
- [1d array to polyline](https://github.com/zeffii/BlenderSciViz/blob/master/intro_script.py), takes array of `(x,y,z)` tuples and generates, edge based mesh (non render)

**3D surface plot**

current limitation: must be even number of verts in x and y direction  

- [1d array to 3D mesh](https://github.com/zeffii/BlenderSciViz/blob/master/points_with_surface_from_n_by_n_grid_of_zheights.py), takes flat array of `(x,y,z)` tuples and generates a mesh (renderable)
- [1d array to 3D mesh, z depends on x and y](https://github.com/zeffii/BlenderSciViz/blob/master/point_surface_z_depends_on_xy_location.py), takes flat array of `(x,y,z)` tuples and generates a mesh (renderable)

- Automatic colour map for 3d mesh data (renderable)

###Useful addons

- [Add Mesh / Add 3d Function Surface](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Add_3d_Function_Surface)


###Todo

    plt.{x,y,z}label,   
    plt.gca, 
    plt.plot(cos(x in range(0,2*pi, 0.01*pi)) ),
