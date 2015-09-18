import bpy
from math import floor

scalar_z = 2.3    #  amplification in z direction
scalar_xy = 1.0   #  amplification in xy


def generate_face_keys(num_x, num_y):
    faces = []
    verts_per_side_x = num_x

    for i in range((num_x - 1) * (num_y - 1)):
        x = (i % (num_x - 1))
        y = floor(i / (num_x - 1))

        level = x + (y * verts_per_side_x)
        idx1 = level
        idx2 = level + 1
        idx3 = level + verts_per_side_x + 1
        idx4 = level + verts_per_side_x
        faces.append([idx1, idx2, idx3, idx4])

    return faces


def geometry_function(image_name):
    img = bpy.data.images[image_name]
    num_x = w = img_width = img.size[0]
    num_y = h = img_height = img.size[1]

    # work on copy only
    pxls = img.pixels[:]
    num_pixels = int(len(pxls) / 4)

    verts = []
    add_vertex = verts.append

    # generator expression
    gen_obj = (i for i in pxls)

    for idx in range(num_pixels):
        y = int(idx / w) * scalar_xy
        x = (idx % w) * scalar_xy
        r = next(gen_obj)
        g = next(gen_obj)
        b = next(gen_obj)
        a = next(gen_obj)

        # height-map, would be grayscale, so z can be set to r*scalar
        z = r * scalar_z
        add_vertex((x, y, z))

    faces = generate_face_keys(num_x, num_y)
    return verts, faces


def generate(func, image_name, geometry_name):
    verts, faces = func(image_name)

    mesh = bpy.data.meshes.new(geometry_name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    obj = bpy.data.objects.new(geometry_name, mesh)
    bpy.context.scene.objects.link(obj)
    obj.select = True
    obj.show_bounds = True


generate(geometry_function, "wvb_flat_2b.png", "3d_Surface_Object")
