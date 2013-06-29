# full runnable example https://gist.github.com/zeffii/5885538

"""
mat:        is a reference to a material  
            ( mat = bpy.data.materials[some_material_name] )
            it must be a :
                - cycles material (and render engine)
                - use_nodes = True

link_str:   'node_name_origin|output_socket > node_name_destination|input_socket'
            easier to think of this as
            'origin > destination' side must include a node name and a socket name or index
            
            if a node has several socketes with the same type (Color, or Vector for example)
            you must specify the socket using an index instead.
            
            The only restriction here is the use of punctuation inside the string. Everything is
            treated as a string, if a string is a reference to an indexed socket, this gets converted
            to a proper integer value automatically.
"""


def make_link(mat, link_str):
    nodes = mat.node_tree.nodes
 
    # strip all trailing and leading whitespaces
    link_str = link_str.strip()
    sockets = link_str.split(">") 
    elements = [socket.strip().split('|') for socket in sockets]
    elements = [[i.strip() for i in c] for c in elements]
    (node_origin, socket_o),(node_dest, socket_i) = elements
    
    # if input or output socket is an integer, cast it.
    if socket_o.isnumeric(): socket_o = int(socket_o)
    if socket_i.isnumeric(): socket_i = int(socket_i)
    
    _output = nodes[node_origin].outputs[socket_o]
    _input = nodes[node_dest].inputs[socket_i]
    mat.node_tree.links.new(_output, _input)
    
    




