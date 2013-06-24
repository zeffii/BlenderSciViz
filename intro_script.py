import bpy
from math import pi, cos

# or a numpy alternative
def frange(start, end, step):
    while start < end:
        yield start
        start += step

# template geometry function    
def geometry_function():
    # these three must have identical number of elements
    verts_x = [cos(x) for x in frange(0, 2*pi, pi*0.01)]
    verts_y = [x for x in frange(-pi, pi, pi*0.01)]
    verts_z = [0 for x in range(len(verts_x))]
    
    # make (x,y,z) coordinate tuples and edge_keys list to
    # daisy-chain the vertices as a polyline
    verts = list(zip(verts_x, verts_y, verts_z))
    edges = [(i, i+1) for i in range(len(verts)-1)]
    
    #faces
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
    
generate(geometry_function, "Polyline_Object")
