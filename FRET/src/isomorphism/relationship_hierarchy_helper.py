from graphs_helper import seril_to_graph, labelled_isomorphism
from graph_tool.all import *

def build_subterm_trees(subgraphs):
    # Get all subterm trees for all subgraphs
    trees = set()
    for subgraph in subgraphs.items():
        subterm_tree = build_subterm_tree(subgraph)
        # graph_draw(subterm_tree,
        #         output_size=(2000,2000),
        #         fit_view=0.9,
        #         vertex_size=10,
        #         vertex_font_size=15,
        #         vertex_aspect=1, 
        #         vertex_text_position=1, 
        #         vertex_text=subterm_tree.vertex_properties["labels"],
        #         output="graph.pdf")
        trees.add(subterm_tree)
    
    # Remove any subterm trees which happen to be subtrees
    # in other trees
    relationship_map = Graph()
    relationship_map_label = relationship_map.new_vertex_property("string") 
    relationship_map.vertex_properties['labels'] = relationship_map_label

    for tree in trees:
        curr_tree_is_encompassing = True
        for tree2 in trees:
            # If tree same as tree2, skip
            if(labelled_isomorphism(tree, tree2)):
                continue
            if(len(subgraph_isomorphism(
                                    tree,
                                    tree2,
                                    subgraph=True,         
                                    induced=True,        
                                    vertex_label=(
                                        tree.vertex_properties['labels'],
                                        tree2.vertex_properties['labels']
                                    ), 
                                    max_n=0                  # We want all matches (n=0 is all matches)
                                    )) != 0):
                curr_tree_is_encompassing = False
                break

        if(curr_tree_is_encompassing):
            relationship_map, props = graph_union(relationship_map,
                                                    tree,
                                                    props=[(
                                                        relationship_map.vertex_properties['labels'],
                                                        tree.vertex_properties["labels"])]
                                                    )
            relationship_map.vertex_properties['labels'] = props[0]

    # Create label -> vertex mapping
    label_map = dict()
    for vertex in relationship_map.vertices():
        vertex_label = relationship_map.vertex_properties['labels'][vertex]
        if(vertex_label in label_map.keys()):
            label_map[vertex_label].append(vertex)
        else:
            label_map[vertex_label] = [vertex]

    # Destroy duplicates
    for label in label_map.keys():
        if(len(label_map[label]) == 1):
            continue

        # Keep first one, rest remove
        vertex_to_keep = label_map[label][0]
        vertices_to_remove = label_map[label][1:]

        # Take care of in-edges, out-edges and vertices
        for vertex in vertices_to_remove:
            # In-edges
            in_edges = vertex.in_edges()
            for in_edge in in_edges:
                source = relationship_map.vertex(in_edge.source())
                relationship_map.remove_edge(in_edge)
                relationship_map.add_edge(source, vertex_to_keep)
        
            # Out-edges
            out_edges = vertex.out_edges()
            for out_edge in out_edges:
                target = relationship_map.vertex(out_edge.target())
                relationship_map.remove_edge(out_edge)
                relationship_map.add_edge(vertex_to_keep, target)      

            # Mark extra vertices
            relationship_map.vertex_properties['labels'][vertex] = 'DUPLICATE'

    # Remove duplicate edges
    remove_parallel_edges(relationship_map)

    # Remove duplicate edges
    vertices_to_remove = []
    for vertex in relationship_map.vertices():
        if(relationship_map.vertex_properties['labels'][vertex] == 'DUPLICATE'):
            vertices_to_remove.append(vertex)
    relationship_map.remove_vertex(reversed(sorted(vertices_to_remove)))

    # Label with counts
    for vertex in relationship_map.vertices():
        curr_tree_label = relationship_map.vertex_properties['labels'][vertex]
        for subg in subgraphs.items():
            curr_subg_label = subg[1][0]  
            if(str(curr_tree_label) == str(curr_subg_label)):
                relationship_map.vertex_properties['labels'][vertex] = f'{curr_tree_label}\n{subg[1][1]}'
                break

    relationship_map_fontsize = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_fontsize[vertex] = 8

    relationship_map_fixedsize = relationship_map.new_vertex_property("bool")
    for vertex in relationship_map.vertices():
        relationship_map_fixedsize[vertex] = False

    relationship_map_height = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_height[vertex] = 1

    relationship_map_width = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_width[vertex] = 1

    graphviz_draw(relationship_map,
        layout="dot",
        vprops={
            'label': relationship_map.vertex_properties['labels'],
            'fontsize': relationship_map_fontsize,
            'fixedsize': relationship_map_fixedsize,
            'height': relationship_map_height,
            'width': relationship_map_width},
        output="graph.pdf")
    
    # graph_draw(relationship_map,
    #     pos = pos,
    #     output_size=(2000,2000),
    #     # fit_view=0.9,
    #     vertex_size=20,
    #     vertex_font_size=15,
    #     vertex_aspect=1, 
    #     vertex_text_position=4, 
    #     vertex_text=relationship_map.vertex_properties["labels"],
    #     output="graph.pdf")
    
    return trees

def build_subterm_tree(graph_json_pair):
    g = Graph()
    vprop_label = g.new_vertex_property("string") 
    seril = graph_json_pair[1][0]

    # If single vertex
    if(type(seril) == str):
        root = g.add_vertex()
        vprop_label[root] = seril
        # Save vertex labels
        g.vertex_properties['labels'] = vprop_label
        return g

    # Add root
    root = g.add_vertex()
    vprop_label[root] = seril

    sub_serils = []
    sub_serils.extend([(root, child) for child in seril[1:]])
    while(len(sub_serils) != 0):
        
        # Get current seril
        parent = sub_serils[0][0]
        curr_subterm = sub_serils[0][1]

        # Add current subterm to tree
        vertex_subterm = g.add_vertex()
        vprop_label[vertex_subterm] = curr_subterm
        g.add_edge(parent, vertex_subterm)

        # If not leaf vertex, add children
        if(not type(curr_subterm) is str):
            # [(root, child) for child in seril[1:]
            sub_serils.extend([(vertex_subterm, child) for child in curr_subterm[1:]])
            
        # Delete seril that's been inspected
        del sub_serils[0]
        if(len(sub_serils) == 0):
            break

    # Save vertex labels
    g.vertex_properties['labels'] = vprop_label
    return g