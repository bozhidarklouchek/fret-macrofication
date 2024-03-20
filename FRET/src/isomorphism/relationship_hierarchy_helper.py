from graphs_helper import seril_to_graph, labelled_isomorphism, string_seril_to_graph
from graph_tool.all import *
from tqdm import tqdm
import csv, json, ast

def build_subterm_trees(subgraphs, min_count=1):
    # Get all subterm trees for all subgraphs
    trees = set()
    for sub in subgraphs.keys():
        if(subgraphs[sub]['count'] >= min_count):
            subterm_tree = build_subterm_tree(subgraphs[sub]['serialisation'])
            trees.add(subterm_tree)
    return trees


def build_subterm_tree(seril):
    g = Graph()
    vprop_label = g.new_vertex_property("string") 

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


def build_relationship_map(trees, subgraphs, draw=True):
    relationship_map = Graph()
    relationship_map_label = relationship_map.new_vertex_property("string") 
    relationship_map.vertex_properties['labels'] = relationship_map_label

    print('Analysing subterms...')
    
    # Remove any subterm trees which happen to be subtrees
    # in other trees
    for tree in tqdm(trees):
        curr_tree_is_encompassing = True
        for tree2 in trees:
            # If tree same as tree2, skip
            if(labelled_isomorphism(tree, tree2)):
                continue
            if(len(subgraph_isomorphism(
                                    tree,
                                    tree2,
                                    subgraph=True,         
                                    induced=False,        
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

    print('Removing duplicate vertices and parallel edges...')
    # Create label -> vertex mapping
    label_map = dict()
    for vertex in tqdm([v for v in relationship_map.vertices()]):
        vertex_string_seril = relationship_map.vertex_properties['labels'][vertex]
        vertex_is_in_map = False

        for label_string_seril in label_map.keys():
            if(labelled_isomorphism(string_seril_to_graph(vertex_string_seril),
                                    string_seril_to_graph(label_string_seril))):
                vertex_is_in_map = True
                label_map[label_string_seril].append(vertex)
                break
        if(not vertex_is_in_map):
            label_map[vertex_string_seril] = [vertex]

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

    # Remove duplicate vertices
    relationship_map.remove_vertex(reversed(sorted(vertices_to_remove)))


    print('Applying label ids...')

    # Label id with counts and apply colors

    for vertex in tqdm([v for v in relationship_map.vertices()]):
        curr_tree_label = relationship_map.vertex_properties['labels'][vertex]
        for sub in subgraphs.keys():
            curr_graph = string_seril_to_graph(curr_tree_label)
            if(labelled_isomorphism(sub, curr_graph)):
                id = subgraphs[sub]['id']
                count = subgraphs[sub]['count']
                relationship_map.vertex_properties['labels'][vertex] = f'{id}\n{count}'
                id += 1
                break

    counts = set()
    colourMap = dict()
    for subg in subgraphs.keys():
        counts.add(subgraphs[subg]['count'])
    counts = sorted(counts, reverse=True)

    for idx, c in enumerate(reversed(counts)):
        colourMap[c] = idx + 1

    maxColourId = len(counts) + 1
    VAL_MAX = 255
    
    # Decide colour depending on count
    relationship_map_fillcolor = relationship_map.new_vertex_property("string")
    for vertex in relationship_map.vertices():
        rgb_val = (0, 0, 0)
        count = int(relationship_map.vertex_properties['labels'][vertex].split('\n')[1])
        colourId = colourMap[count]
        val = int((colourId / maxColourId) * 255 * 5)
        if(val >= 0 and val <= VAL_MAX):
            rgb_val = (255, int(val/5), 0)
        elif(val >= VAL_MAX + 1 and val <= VAL_MAX * 2):
            rgb_val = (255 - int(val/5), 255, 0)
        elif(val >= VAL_MAX * 2 + 1 and val <= VAL_MAX * 3):
            rgb_val = (0, 255, int(val/5))
        elif(val >= VAL_MAX * 3 + 1 and val <= VAL_MAX * 4):
            rgb_val = (0, 255 - int(val/5), 255)
        elif(val >= VAL_MAX * 4 + 1 and val <= VAL_MAX * 5):
            rgb_val = (int(val/5), 0, 255)

        relationship_map_fillcolor[vertex] = str('#%02x%02x%02x' % rgb_val)

    relationship_map_fontsize = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_fontsize[vertex] = 64

    relationship_map_fixedsize = relationship_map.new_vertex_property("bool")
    for vertex in relationship_map.vertices():
        relationship_map_fixedsize[vertex] = False

    relationship_map_height = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_height[vertex] = 1

    relationship_map_width = relationship_map.new_vertex_property("int")
    for vertex in relationship_map.vertices():
        relationship_map_width[vertex] = 1

    if(draw):
        graphviz_draw(relationship_map,
            layout="dot",
            vprops={
                'label': relationship_map.vertex_properties['labels'],
                'fillcolor': relationship_map_fillcolor,
                'fontsize': relationship_map_fontsize,
                'fixedsize': relationship_map_fixedsize,
                'height': relationship_map_height,
                'width': relationship_map_width},
            output="../output/relationship_map.pdf")
    