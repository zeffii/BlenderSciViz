# full runnable example https://gist.github.com/zeffii/5885538

"""
mat:        is a reference to a material  
            ( mat = bpy.data.materials[some_material_name] )
            it must be a :
                - cycles material (and render engine)
                - use_nodes = True

link_str:   'node_name_origin|output_socket > node_name_destination|input_socket'
            easier to think of this as
            'origin > destination' each side must include a node name and a socket name or index.
            
            if a node has several sockets with the same type (Color, or Vector for example)
            you must specify the socket using an index instead.
            
            The only restriction here is the use of punctuation inside the string. Everything is
            treated as a string, if a string is a reference to an indexed socket this gets converted
            to a proper integer value automatically.
"""


import bpy

def make_link(mat, link_str):
    nodes = mat.node_tree.nodes
 
    # Geometry|Position > ADD_0|0
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


