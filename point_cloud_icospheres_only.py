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
    
    coords = []
    num_random_points = 300
    [coords.append(rnd_coords()) for i in range(num_random_points)]

    return coords

def generate_objects(func, geometry_name):
    coords = func()

    # get icosphere mesh, deleting the object doesn't delete the mesh.
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, size=0.05)
    obj = bpy.context.active_object
    mesh = obj.data
    mesh.name = 'SciVizIcoSphere'
    bpy.ops.object.delete(use_global=False)
    
    # new objects, sharing icosphere mesh
    for coordinate in coords:
        obj = bpy.data.objects.new(geometry_name, mesh)  
        obj.location = coordinate
          
        scene = bpy.context.scene    
        scene.objects.link(obj)    
    

    
    
generate_objects(geometry_function, "PointCloud_Object")
