import bpy
from math import pi, cos, floor
import random

# or a numpy alternative
def frange(start, end, step):
    while start < end:
        yield start
        start += step

def generate_face_keys(num_x, num_y):
    faces = []

    for i in range((num_x-1)*(num_y-1)):
        x = (i % (num_x-1))
        y = floor(i / (num_x-1))
        verts_per_side_x = num_x

        level = x + (y*verts_per_side_x)
        idx1 = level
        idx2 = level + 1
        idx3 = level + verts_per_side_x + 1
        idx4 = level + verts_per_side_x
    
        faces.append([idx1, idx2, idx3, idx4])

    return faces

# template geometry function    
def geometry_function():

    def get_x(i):
        return x_limits[0] + x_offset * (i % num_x)
    
    def get_y(i):
        return y_limits[0] + y_offset * floor(i / num_x)

    rnd_comp = lambda: random.uniform(-0.1,0.1)
    rnd_coords = lambda: rnd_comp()

    x_limits = [-6, 6]
    y_limits = [-2, 2]
    x_range = max(x_limits) - min(x_limits)
    y_range = max(y_limits) - min(y_limits)
    num_x = 6
    num_y = 6
    x_offset = x_range / num_x
    y_offset = y_range / num_y
    
    num_points = num_x * num_y

    # verts 
    verts_z = [rnd_coords() for i in range(num_points)]
    verts_x = [get_x(i) for i in range(num_points)]
    verts_y = [get_y(i) for i in range(num_points)]    
    verts = list(zip(verts_x, verts_y, verts_z))
    
    # faces, this is a little trickier
    faces = generate_face_keys(num_x, num_y)
    return verts, faces

def generate(func, geometry_name):
    verts, faces = func()

    mesh = bpy.data.meshes.new(geometry_name + "_mesh")  
    mesh.from_pydata(verts, [], faces)  
    mesh.update() 
      
    obj = bpy.data.objects.new(geometry_name, mesh)  
      
    scene = bpy.context.scene    
    scene.objects.link(obj)    
    obj.select = True
    obj.show_bounds = True # optional

    
generate(geometry_function, "3d_Surface_Object")
