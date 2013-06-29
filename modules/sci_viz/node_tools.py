import bpy

def make_link(mat, link_str):
    nodes = mat.node_tree.nodes
 
    # Geometry|Position > ADD_0|0
    link_str = link_str.strip()
    sockets = link_str.split(">") 
    sockets = [socket.strip() for socket in sockets]
    node_origin, output_socket = sockets[0].split('|')
    node_destination, input_socket = sockets[1].split('|')    
    
    # make sure no spaces.
    node_origin = node_origin.strip()
    output_socket = output_socket.strip()
    node_destination = node_destination.strip()
    input_socket = input_socket.strip()
    
    # if input or output socket is an integer, cast it.
    if output_socket.isnumeric():
        output_socket = int(output_socket)
    
    if input_socket.isnumeric():
        input_socket = int(input_socket)    
    
    output = nodes[node_origin].outputs[output_socket]
    input = nodes[node_destination].inputs[input_socket]
    mat.node_tree.links.new(output, input)
