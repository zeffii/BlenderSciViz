import bpy
from math import pi, cos
import random
import bmesh

'''
- generate a icosphere mesh from bmesh, 
- create a new object for each coordinate, but reusing the same mesh

pro: low memory footprint (due to reuse)
con: large quantity of Objects, means 'name collision' checking will still
     be a slowing factor at creation time.

alt: Alternativly you can make a single object using the coordinates and place
     duplicates at each vertex. 
        
        See dupliverts_example.py

'''


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

    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2, diameter=0.05)
    mesh = bpy.data.meshes.new('SciVizIcoSphere_mesh')
    bm.to_mesh(mesh)
    bm.free()
    mesh.use_fake_user = True  # just in case
    
    # new objects, sharing icosphere mesh
    for coordinate in coords:
        obj = bpy.data.objects.new(geometry_name, mesh)  
        obj.location = coordinate
          
        scene = bpy.context.scene    
        scene.objects.link(obj)

generate_objects(geometry_function, 'random_spheres')
