from graph_tool.all import *
import cairo
from tqdm import tqdm

# Unsure about U, V
UNORDERED = {'&', '|', 'XOR', '<->', '<=>',
             '=', '!=', '*', '+'}
ORDERED = {'->', '=>', 'ifThen', 'atPrevOccurrenceOf',
           'atNextOccurrenceOf', '^', '-', '<', '<=',
           '>', '>=', '!', '~', 'Y', 'H', 'O', 'G',
           'X', 'F', '/'}
PARTIAL = {'partial_test': 3, 'partial_test2': 5}
UNORDERED_LABEL = '*'

def add_subgraphs(seril, SUBGRAPHS):
    sub_serils = [seril]
    while(len(sub_serils) != 0):
        
        # Get current seril
        curr_seril = sub_serils[0]

        # If not leaf vertex, add children
        if(not type(curr_seril) is str):
            sub_serils.extend(curr_seril[1:])
            
        # Create current subgraph
        curr_subg = seril_to_graph(sub_serils[0])

        # Check if already in dict
        curr_is_unique = True
        for unique_subg in SUBGRAPHS.keys():
            if(labelled_isomorphism(unique_subg, curr_subg)):
                curr_is_unique = False
                break
        if(curr_is_unique):
            SUBGRAPHS[curr_subg] = (curr_seril, 0)
        
        # Delete seril that's been inspected
        del sub_serils[0]
        if(len(sub_serils) == 0):
            break

def build_tree(g, vprop_label, vcolor, eprop_label, seril):
    parent = g.add_vertex()

    # Add vertex properties
    vprop_label[parent] = seril[0]
    vcolor[parent] = "#2ec27e"

    childNum = 1
    edge_label = ''
    for subseq_seril in seril[1:]:
        # Apply UNORDERED_LABEL if operator is unordered
        if(seril[0] in UNORDERED):
            edge_label = UNORDERED_LABEL
        # Apply child number as label if operator is ordered
        elif(seril[0] in ORDERED):
            edge_label = str(childNum)
            childNum += 1
        # Apply:
        # - child number as label if child count is below opeartor's ordered count
        # - UNORDERED_LABEL otherwise
        elif(seril[0] in PARTIAL.keys()):
            if(childNum <= PARTIAL[seril[0]]):
                edge_label = str(childNum)
                childNum += 1
            else:
                edge_label = UNORDERED_LABEL


        # Don't call recursive function if curr child is leaf vertex
        if(type(subseq_seril) == str):
            child = g.add_vertex()
            vprop_label[child] = subseq_seril
            vcolor[child] = "#2ec27e"

            e = g.add_edge(parent, child)
            eprop_label[e] = edge_label
        # Call recursively on children's children
        else:
            p = build_tree(g, vprop_label, vcolor, eprop_label, subseq_seril)
            e = g.add_edge(parent, p)
            eprop_label[e] = edge_label
        
    return parent

def apply_coords(parent, tree_depth, coords, x, y):
    y = y + 1
    children = [child for child in parent.out_neighbors()]
    width = (len(children) - 1) * (tree_depth) * (1/y)
    start_x = x - width / 2
    for child in children:
        coords[child] = [start_x, y]
        apply_coords(child, tree_depth, coords, start_x, y)
        start_x += (tree_depth) * (1/y)

def calculate_draw_coords(g, root):
    coords = g.new_vertex_property("vector<double>") 
    vertices = [root, 'end']
    space = 3
    sp = 1
    w = 0
    x = 0
    y = 0
    
    while(len(vertices) != 0):
        curr_vertex = vertices[0]
        if(type(curr_vertex) == str and curr_vertex == 'end'):
            y += 1
            del vertices[0]
            if(len(vertices) == 0): break
            else:
                w = len(vertices)
                vertices.append('end')
                x = - ((w - 1) / 2)
        elif(type(curr_vertex) == str and curr_vertex == 'space'):
            del vertices[0]
            x += space

        else:
            curr_vertex = vertices[0]
            coords[curr_vertex] = [x, y]

            children = [child for child in curr_vertex.out_neighbors()]
            vertices.extend(children)
            vertices.append('space')
            x += sp
            del vertices[0]
    return coords

def seril_to_graph(seril, draw=False):
    # Graph setup
    g = Graph()
    vprop_label = g.new_vertex_property("string") 
    vcolor = g.new_vp("string")
    eprop_label = g.new_edge_property("string") 

    root = None
    # If graph only with single vertex
    if(type(seril) == str):
        root = g.add_vertex()
        vprop_label[root] = seril
        vcolor[root] = "#1c71d8"
    # Else build up tree recursively
    else: 
        # Get root and add different colour
        root = build_tree(g, vprop_label, vcolor, eprop_label, seril)
        vcolor[root] = "#1c71d8"

    # Save properties
    g.vertex_properties['labels'] = vprop_label
    g.vertex_properties['color'] = vcolor
    g.edge_properties['labels'] = eprop_label

    coords = calculate_draw_coords(g, root)

    if(draw):
        graph_draw(g,
                pos=coords,
                output_size=(2000,2000),
                fit_view=0.9,
                # fit_view_ink=True,
                vertex_aspect=1, 
                vertex_text_position=1, 
                vertex_text_color='black',
                vertex_font_family='sans',
                vertex_font_size=15,
                vertex_font_weight=cairo.FONT_WEIGHT_NORMAL,
                vertex_color=None,
                vertex_size=10,
                vertex_text=vprop_label,
                vertex_fill_color=vcolor,
                edge_pen_width=2,
                edge_text=eprop_label,
                edge_font_size=15,
                output="graph.pdf")

    return g

def labelled_isomorphism(g1, g2):                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
  if not g1.num_vertices() == g2.num_vertices():                                                                                 
    return False                                                                                                
  if not g1.num_edges() == g2.num_edges(): 
    return False 

  sub = g1
  graph = g2 
  v_labels = (sub.vertex_properties["labels"], graph.vertex_properties["labels"])
  e_labels = (sub.edge_properties["labels"], graph.edge_properties["labels"])

  return subgraph_isomorphism(sub, graph, subgraph=False, induced=True, vertex_label=v_labels, edge_label=e_labels, max_n=1)

def get_graph_data(serils):
    graphs = []
    SUBGRAPHS = {}

    print('Constructing parent graphs...')

    # Construct graph and extract subgraphs for each seril
    for seril in tqdm(serils):
        if(seril is not None):
            g = seril_to_graph(seril, True)
            graphs.append(g)
            add_subgraphs(seril, SUBGRAPHS)
    return graphs, SUBGRAPHS
    