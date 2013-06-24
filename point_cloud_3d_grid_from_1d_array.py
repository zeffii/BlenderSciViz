import bpy
from math import pi, cos, floor
import random

# or a numpy alternative
def frange(start, end, step):
    while start < end:
        yield start
        start += step

# template geometry function    
def geometry_function():

    rnd_comp = lambda: random.uniform(-0.3,0.3)
    rnd_coords = lambda: rnd_comp()

    x_limits = [-6, 6]
    y_limits = [-6, 6]
    x_range = max(x_limits) - min(x_limits)
    y_range = max(y_limits) - min(y_limits)
    num_x = 50
    num_y = 50
    x_offset = x_range / num_x
    y_offset = y_range / num_y
    
    num_points = num_x * num_y

    def get_x(i):
        return x_limits[0] + x_offset * (i % num_x)
    
    def get_y(i):
        return y_limits[0] + y_offset * floor(i / num_x)
 
    verts_z = [rnd_coords() for i in range(num_points)]
    verts_x = [get_x(i) for i in range(num_points)]
    verts_y = [get_y(i) for i in range(num_points)]    

    verts = list(zip(verts_x, verts_y, verts_z))
    return verts, []

def generate(func, geometry_name):
    verts, faces = func()

    mesh = bpy.data.meshes.new(geometry_name + "_mesh")  
    mesh.from_pydata(verts, [], [])  
    mesh.update() 
      
    obj = bpy.data.objects.new(geometry_name, mesh)  
      
    scene = bpy.context.scene    
    scene.objects.link(obj)    
    obj.select = True
    obj.show_bounds = True # optional

    
generate(geometry_function, "3d_Surface_Object")
