"""
mat:        is a reference to a material  
            ( mat = bpy.data.materials[some_material_name] )
            it must be a :
                - cycles material (and render engine)
                - use_nodes = True

link_str:   'node_name_origin|output_socket > node_name_destination|input_socket'
            easier to think of this as 'origin > destination' each side must include:
                - a node name/index 
                - a socket name/index
                        
            If a node has several sockets with the same type (Color, or Vector for example)
            you must specify the socket using an index instead.

            For example, a link_str might look like these
            'ColorRamp|Color > Diffuse BSDF|Color'
            'ColorRamp|0 > Diffuse BSDF|0'
            'ColorRamp.001|0 > Some_Renamed_Node|0'
            '0|0 > 1|0'
            
            Each node can be referenced by name or index, usually directly specifying the name will be
            clearer to you later. Input and Output sockets are also named and indexed. Because a node 
            can have several identically named sockets (like several color input sockets) you have to
            specify them using their index.


example use:
            
            from sci_viz.node_tools import make_link
            
            mat = bpy.data.materials[some_material_name]
            make_link(mat, 'ColorRamp|Color > Diffuse BSDF|Color')

            # full runnable example https://gist.github.com/zeffii/5885538            
"""

import bpy

def make_link(mat, link_str):
    nodes = mat.node_tree.nodes
 
    # split incoming link_str into nodes and sockets
    link_str = link_str.strip()
    sockets = link_str.split(">") 
    sockets = [socket.strip() for socket in sockets]
    node_origin, output_socket = sockets[0].split('|')
    node_destination, input_socket = sockets[1].split('|')    
    
    # make sure no spaces, and cast as int if needed
    identifiers = [node_origin, output_socket, node_destination, input_socket]
    identifiers = [i.strip() for i in identifiers]
    identifiers = [(int(i) if i.isnumeric() else i) for i in identifiers]
    node_origin, output_socket, node_destination, input_socket = identifiers

    output = nodes[node_origin].outputs[output_socket]
    input = nodes[node_destination].inputs[input_socket]
    mat.node_tree.links.new(output, input)
