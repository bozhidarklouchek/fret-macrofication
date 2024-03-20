from graph_tool.all import *

from data_helper import read_seril_json, write_subterm_count, write_id_to_subterm_map
from graphs_helper import get_graph_data
from counter import update_subgraph_state
from relationship_hierarchy_helper import build_subterm_trees, build_relationship_map


# READ DATA
serialisations = read_seril_json('../../output/serialisation.json')


# BUILD SUBGRAPHS, FIND SUBTERMS

# Exract graph data
# - graph representations of all serilisations
# - all subgraphs from those graphs
graphs, subgraphs = get_graph_data(serialisations)

# Update counts of subgraphs occurrences within parent graphs
update_subgraph_state(graphs, subgraphs)

# Build subterm trees to build relationship graph
subterm_trees = build_subterm_trees(subgraphs)

# Build relationship graph
build_relationship_map(subterm_trees, subgraphs)


# SAVE RESULT

# Subgraph occurrence result sorted in a descending order
write_subterm_count(subgraphs)




