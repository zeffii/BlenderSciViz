import bpy
from math import pi, cos
import random

# or a numpy alternative
def frange(start, end, step):
    while start < end:
        yield start
        start += step

# template geometry function    
def geometry_function():

    rnd_comp = lambda: random.uniform(-4,4)
    rnd_coords = lambda: [rnd_comp() for i in range(3)]
    
    verts = []
    num_random_points = 300
    [verts.append(rnd_coords()) for i in range(num_random_points)]
    
    print(verts)
    
    edges = []
    faces = []
    return verts, edges, faces

def generate(func, geometry_name):
    verts, edges, faces = func()
    
    mesh = bpy.data.meshes.new(geometry_name + "_mesh")  
    mesh.from_pydata(verts, edges, faces)  
    mesh.update() 
      
    obj = bpy.data.objects.new(geometry_name, mesh)  
      
    scene = bpy.context.scene    
    scene.objects.link(obj)    
    obj.select = True
    obj.show_bounds = True # optional
    
    
generate(geometry_function, "PointCloud_Object")
