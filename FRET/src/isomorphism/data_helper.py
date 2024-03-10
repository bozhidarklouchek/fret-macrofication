import json, csv

RESULT_PATH = '../output/{0}'

def read_seril_json(path):
    print('Reading serialised input...')
    # Read the JSON file
    with open(path, 'r') as file:
        # Load JSON data from the file
        data = json.load(file)
        serils = [seril['serialisation'] for seril in data]
    print(f'I successfully read {len(serils)} serialisations.', end=' ')

    valid_serils = [s for s in serils if s is not None]
    print(f'{len(valid_serils)}/{len(serils)} are valid.')
    return valid_serils

def write_subterm_count(subgraphs):
    path = RESULT_PATH.replace('{0}', 'subgraph_count.csv')
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['count', 'serialisation'])
        # Write each row separately to a CSV file
        for _, subg_details in sorted(subgraphs.items(), key=lambda item: item[1]['count'], reverse=True):
            writer.writerow([subg_details['id'], subg_details['serialisation'], subg_details['count']])
    print(f'Subterm count has been saved to {path}')
