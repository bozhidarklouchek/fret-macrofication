from pathlib import Path
import sys, json, csv
sys.path.append('./serialiser')
sys.path.append('./isomorphism')
sys.path.append('../../grammar')

from fret_reader import getReqts
from fret_serialiser import addSerilisationToReqts
from verifier import verify_serilisations
from graph_tool.all import *
from data_helper import read_seril_json, write_subterm_count
from graphs_helper import get_graph_data
from counter import update_subgraph_state
from relationship_hierarchy_helper import build_subterm_trees, build_relationship_map


SAVE_RESULT = True

print()
print('*** SERIALISATION STEP ***')
reqts, readFormulasCount = getReqts(sys.argv[1])
if(len(reqts) != 0):
    reqts_with_serilisations, serialisedFormulasCount = addSerilisationToReqts(reqts, readFormulasCount)
    verify_serilisations(reqts_with_serilisations, serialisedFormulasCount)
    if(SAVE_RESULT):
        result = [{k : v for k,v in reqt.items() if k != 'evaluatedSerialisation' and k != 'evaluatedFret'} for reqt in reqts_with_serilisations]
        Path("../output").mkdir(parents=True, exist_ok=True)
        # Save to .json
        with open('../output/serialisation.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        # Save to .csv
        with open('../output/serialisation.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result[0].keys())
            for res in result:
                writer.writerow(res.values())

print()
print('*** ISOMORPHISM STEP ***')
# READ DATA
serialisations = read_seril_json('../output/serialisation.json')


# BUILD SUBGRAPHS, FIND SUBTERMS

# Exract graph data
# - graph representations of all serilisations
# - all subgraphs from those graphs
graphs, subgraphs = get_graph_data(serialisations)

# Update counts of subgraphs occurrences within parent graphs
update_subgraph_state(graphs, subgraphs)

# Build subterm trees to build relationship graph
subterm_trees = build_subterm_trees(subgraphs)

label_mappings = build_relationship_map(subterm_trees, subgraphs)


# SAVE RESULT

# Subgraph occurrence result sorted in a descending order
write_subterm_count(subgraphs)
# Subgraph occurrence result sorted in a descending order
# write_id_to_subterm_map(label_mappings)



