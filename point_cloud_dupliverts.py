import bpy
from math import pi, cos
import random
import bmesh

'''
- generate a single object using coordinates (let's call it a 'point cloud object')
- promote the object to a parent and use duplication on each vertex to 
  place icospheres

pro:  - single object creation is fast
      - using blender built in duplication (dupliverts) means you get good
        performance too
cons: - the main annoyance is that the primal child object (the one being 
        duplicated) will show up in the 3dview. But it not in the Rendered view.

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

    objects = bpy.data.objects
    scene = bpy.context.scene
    meshes = bpy.data.meshes
    
    coords = func()

    # make parent object
    parent_mesh = meshes.new('parent_mesh')
    parent_mesh.from_pydata(coords, [], [])
    parent_obj = objects.new(geometry_name, parent_mesh)
    
    # make child object
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2, diameter=0.05)
    child_mesh = meshes.new('SciVizIcoSphere_mesh')
    child_obj = objects.new('ico_obj', child_mesh)
    bm.to_mesh(child_mesh)
    bm.free()
        
    scene.objects.link(parent_obj)      
    scene.objects.link(child_obj)
    
    child_obj.parent = parent_obj
    parent_obj.dupli_type = 'VERTS'

generate_objects(geometry_function, 'random_spheres')
