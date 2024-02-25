from graph_tool.all import *

from data_helper import read_seril_json, write_result
from graphs_helper import get_graph_data
from counter import update_subgraph_state


# Read serilisation data
serialisations = read_seril_json('../../output/serialisation.json')

# Exract graph data
# - graph representations of all serilisations
# - all subgraphs from those graphs
graphs, subgraphs = get_graph_data(serialisations)

# Update counts of subgraphs occurrences within parent graphs
update_subgraph_state(graphs, subgraphs)

# Save subgraph occurrence result sorted in a descending order
write_result(subgraphs)



