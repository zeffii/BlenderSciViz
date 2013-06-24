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

    num_points = 300

    rnd_comp = lambda: random.uniform(-4,4)
    rnd_coords = lambda: [rnd_comp() for i in range(3)]
    coords = [rnd_coords() for i in range(num_points)]

    rnd_rgba = lambda: [random.random() for i in range(4)]
    colors = [rnd_rgba() for i in range(num_points)]

    return coords, colors

def generate_objects(func, geometry_name):
    coords, colors = func()

    # get icosphere mesh, deleting the object doesn't delete the mesh.
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, size=0.05)
    obj = bpy.context.active_object
    mesh = obj.data
    mesh.name = 'SciVizIcoSphere'
    bpy.ops.object.delete(use_global=False)
    
    # new objects, sharing icosphere mesh
    for coordinate, color in zip(coords, colors):
        obj = bpy.data.objects.new(geometry_name, mesh)  
        obj.location = coordinate
        obj.color = color
                  
        scene = bpy.context.scene    
        scene.objects.link(obj)
 
    
generate_objects(geometry_function, "PointCloud_Object")
