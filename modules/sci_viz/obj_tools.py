import bpy
from mathutils import Vector, Color
from collections import defaultdict

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


def avg_col(cols):
    avg_col = Color((0.0, 0.0, 0.0))
    for col in cols:
        avg_col += col/len(cols)
    return avg_col


class VertexColors:
    """
    usage: 
    from sci_viz import obj_tools
    vc_obj = obj_tools.VertexColors()

    import pprint
    pprint.pprint(vc_obj.vcols_avg)

    input:
    - can be passed an arbitrary mesh object, and named vertex color map, but
      will use active_object and 'Col' if none specified.

    output:
    - vcols will output a dict of vertex indices and the colors associated with them
    - vcols_avg will output the dict with all colors for averaged per vertex.
    """

    def __init__(self, obj=bpy.context.active_object, col='Col'):

        self.tk = defaultdict(list)

        mesh = obj.data
        color_layer = mesh.vertex_colors[col]

        i = 0
        for poly in mesh.polygons:
            for idx in poly.loop_indices:
                loop = mesh.loops[idx]
                color = color_layer.data[i].color
                self.tk[loop.vertex_index].append(color)
                i += 1

    @property
    def vcols(self):
        return self.tk

    @property
    def vcols_avg(self):
        return {k: avg_col(v) for k, v in self.tk.items()}



