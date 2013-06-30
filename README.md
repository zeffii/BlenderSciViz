BlenderSciViz
=============

Preliminary code for plotting data in Blender.

###What this project hopes to achieve?  
Show various ways in which the Blender Python API, called `bpy`, can be used to generate meshes, shaders and vector graphics. 
These examples are intended to help you code your own visualizations, and can be used on their own or as part of the `sci_viz` module.

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

- [1d array to 3D mesh](https://github.com/zeffii/BlenderSciViz/blob/master/points_with_surface_from_n_by_n_grid_of_zheights.py), takes flat array of `(x,y,z)` tuples and generates a mesh (renderable)
- [1d array to 3D mesh, z depends on x and y](https://github.com/zeffii/BlenderSciViz/blob/master/point_surface_z_depends_on_xy_location.py), takes flat array of `(x,y,z)` tuples and generates a mesh (renderable)
- [Automatic height to gradient colour map for 3d mesh data](https://github.com/zeffii/BlenderSciViz/blob/master/materials_color_from_z_domain.py), takes the world or local bounds of the object and creates a shader automatically with a colour ramp (renderable)

**Node scripting**
- [mini node connection grammar](https://github.com/zeffii/BlenderSciViz/blob/master/node_connection_grammar.py), simplifies connecting existing nodes. example grammar: `"Node.001|Color > MixRGB.002|0"`. Full grammar specs are in the file.

**General obj utility scripts**
- [bounding box tools](https://github.com/zeffii/BlenderSciViz/blob/master/obj_tools_bounding_box.py), provides `mix, max and distance` for an object, calculated in world or local coordinates

**The sci_viz module**  
The `sci_viz` module can be placed inside the blender scripts folder like `../scripts/modules/sci_viz` , to conveniently import the various utilities. 
For example if you need to make a bunch of node links in add these lines to the top of your python script and you can use the **node mini grammar** to connect nodes.

    import sci_viz 
    from sci_viz.node_tools import make_link
    

###Gallery

![waveform zheight shader][1]



###Useful addons

- [Add Mesh / Add 3d Function Surface](http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Add_Mesh/Add_3d_Function_Surface)

  [1]: http://i.imgur.com/l8ZWAkp.png

