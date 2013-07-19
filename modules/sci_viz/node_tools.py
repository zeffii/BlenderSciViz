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
