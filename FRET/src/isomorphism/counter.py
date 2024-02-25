from graph_tool.all import *
from tqdm import tqdm

from graphs_helper import labelled_isomorphism

def update_subgraph_state(graphs, SUBGRAPHS):

    print('Analysing subgraphs...')

    # For each graph, look for subgraphs and add to count dict
    for graph in tqdm(graphs):
        # g = seril_to_graph(serils[0], draw=True)
        for sub in SUBGRAPHS.keys():

            # If graphs are the same, add 1 and continue
            if(labelled_isomorphism(sub, graph)):
                SUBGRAPHS[sub] = (SUBGRAPHS[sub][0], SUBGRAPHS[sub][1] + 1)
                continue

            # Get graph properties
            v_labels = (sub.vertex_properties["labels"],
                        graph.vertex_properties["labels"])
            e_labels = (sub.edge_properties["labels"],
                        graph.edge_properties["labels"])

            isomorphisms = subgraph_isomorphism(
                                    sub,
                                    graph,
                                    subgraph=True,         
                                    induced=True,        
                                    vertex_label=v_labels,
                                    edge_label=e_labels, 
                                    max_n=0                  # We want all matches (n=0 is all matches)
                                    )

            for isomorphism in isomorphisms:
                SUBGRAPHS[sub] = (SUBGRAPHS[sub][0], SUBGRAPHS[sub][1] + 1)
