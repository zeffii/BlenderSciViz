import bpy
from math import pi, cos

# or a numpy alternative
def frange(start, end, step):
    while start < end:
        yield start
        start += step
    
def geometry_function():
    # these three must have identical number of elements
    verts_x = [cos(x) for x in frange(0, 2*pi, pi*0.01)]
    verts_y = [x for x in frange(-pi, pi, pi*0.01)]
    verts_z = [0 for x in range(len(verts_x))]
    
    # make (x,y,z) coordinate tuples and edge_keys list to
    # daisy-chain the vertices as a polyline
    verts = list(zip(verts_x, verts_y, verts_z))
    edges = [(i, i+1) for i in range(len(verts)-1)]
    return verts, edges

def make_polyline(func, polyline_name):
    verts, edges = func()
    
    mesh = bpy.data.meshes.new("polyline_edge_mesh")  
    mesh.from_pydata(verts, edges, [])  
    mesh.update() 
      
    polyline_object = bpy.data.objects.new(polyline_name, mesh)  
      
    scene = bpy.context.scene    
    scene.objects.link(polyline_object)    
    polyline_object.select = True    
    
make_polyline(geometry_function, "Polyline_Object")
