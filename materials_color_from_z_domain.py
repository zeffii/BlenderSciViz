import bpy
import sci_viz
from sci_viz.node_tools import make_link
from sci_viz.obj_tools import bounds

"""
This generates a cycles shader that will colour ramp from black to white (default) according to the extent of the
3d obj it's being pointed at.

"""

def create_cycles_material(settings):
    
    scn = bpy.context.scene
    if not scn.render.engine == 'CYCLES':
        scn.render.engine = 'CYCLES'
 
    mat = bpy.data.materials.new(settings.name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
 
    '''Make or move nodes'''
    node = nodes['Diffuse BSDF']
    node.location = 600, 120
    
    node = nodes['Material Output']
    node.location = 800, 120
    
    node = nodes.new('ShaderNodeNewGeometry')
    node.name = 'Geometry_0'
    node.location = -300, 120
    
    node = nodes.new('ShaderNodeVectorMath')
    node.operation = 'ADD'
    node.label = 'ADD'
    node.name = 'ADD_0'
    node.inputs[1].default_value = settings.vector_add   
    node.location = -100, 120
    
    node = nodes.new('ShaderNodeVectorMath')
    node.operation = 'DOT_PRODUCT'
    node.label = 'DOT'    
    node.name = 'DOT_0'
    node.inputs[1].default_value = settings.vector_dot
    node.location = 100, 120
    
    node = nodes.new('ShaderNodeValToRGB')
    node.location = 300, 120
 
    # using connection grammar    
    connection_list = [
        'Geometry_0|Position > ADD_0|0',
        'ADD_0|Vector > DOT_0|0',
        'DOT_0|Value > ColorRamp|Fac',
        'ColorRamp|Color > Diffuse BSDF|Color'
    ]
 
    for link in connection_list:
        make_link(mat, link)

def create_settings(obj, material_name):
    object_details = bounds(obj)
    z_offset = -object_details.z.min

    settings = lambda: None
    settings.name = material_name
    settings.vector_add = (0, 0, z_offset)
    settings.vector_dot = (0, 0, 1.0 / object_details.z.distance)
    return settings

obj = bpy.data.objects['3d_Surface_Object']
settings = create_settings(obj, 'zheight3')
create_cycles_material(settings)
