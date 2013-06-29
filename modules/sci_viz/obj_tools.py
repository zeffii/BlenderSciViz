import bpy
from mathutils import Vector

def bounds(obj, local=False):
    """ 
    usage:
    
    obj = bpy.context.object
    object_details = bounds(obj, False)

    a = object_details.z.max
    b = object_details.z.min
    c = object_details.z.distance

    print(a, b, c)

    """

    local_coords = obj.bound_box[:]
    om = obj.matrix_world

    if not local:    
        worldify = lambda p: om * Vector(p[:]) 
        coords = [worldify(p).to_tuple() for p in local_coords]
    else:
        coords = [p[:] for p in local_coords]
        
    rotated = zip(*coords[::-1])
    
    push_axis = []
    for (axis, _list) in zip('xyz', rotated):
        info = lambda: None
        info.max = max(_list)
        info.min = min(_list)
        info.distance = info.max - info.min
        push_axis.append(info)
    
    import collections
    
    originals = dict(zip(['x', 'y', 'z'], push_axis))
     
    o_details = collections.namedtuple('object_details', 'x y z')
    return o_details(**originals)

