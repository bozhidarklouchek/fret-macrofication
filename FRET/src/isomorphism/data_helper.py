import json, csv

RESULT_PATH = '../../output/subgraph_count.csv'

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

def write_result(subgraphs):
    print('Saving result...')
    with open(RESULT_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['count', 'serialisation'])
        # Write each row separately to a CSV file
        for _, seril_and_count  in sorted(subgraphs.items(), key=lambda item: item[1][1], reverse=True):
            writer.writerow([seril_and_count[1], seril_and_count[0]])
    print(f'Result has been saved to {RESULT_PATH}')
