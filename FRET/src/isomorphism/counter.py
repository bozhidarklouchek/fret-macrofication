from graph_tool.all import *
from tqdm import tqdm

from graphs_helper import labelled_isomorphism

def update_subgraph_state(graphs, subgraphs):

    # Initialise subgraph dictionary
    # for sub in subgraphs.keys():
    #     subgraphs[sub] = {'id': -1, 'serialisation':'', 'count': 0}

    print('Extracting subgraphs...')
    # For each graph, look for subgraphs and add to count dict
    for graph in tqdm(graphs):
        for sub in subgraphs.keys():

            # If graphs are the same, add 1 and continue
            if(labelled_isomorphism(sub, graph)):
                subgraphs[sub] = {'id': -1,
                                  'serialisation': subgraphs[sub]['serialisation'],
                                  'count': subgraphs[sub]['count'] + 1}
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
                                    induced=False,        
                                    vertex_label=v_labels,
                                    edge_label=e_labels, 
                                    max_n=0                  # We want all matches (n=0 is all matches)
                                    )

            for isomorphism in isomorphisms:
                subgraphs[sub] = {'id': -1, 'serialisation': subgraphs[sub]['serialisation'], 'count': subgraphs[sub]['count'] + 1}

    # Order based on count
    subgraphs_ordered = sorted(subgraphs.items(), key=lambda item: item[1]['count'], reverse=True)

    # Add id in subgraphs object
    for idx, subg_ordered in enumerate(subgraphs_ordered):
        subgraphs[subg_ordered[0]]['id'] = idx + 1

    # Add shrink_power information
    for sub in subgraphs.keys():
        occurrence_count = subgraphs[sub]['count']
        subterm_size = len([v for v in sub.vertices()])
        shrink_power = occurrence_count * subterm_size
        subgraphs[sub]['shrinking_power'] = shrink_power
