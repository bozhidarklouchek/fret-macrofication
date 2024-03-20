import json, csv, os
from collections import defaultdict

RESULT_PATH = '../output/{0}'

def is_only_unary_operations(subgraph):
    source_dict = defaultdict(int)
    target_dict = defaultdict(int)

    for edge in subgraph.edges():
        src = edge.source()
        if(source_dict[src] != 0):
            return False
        source_dict[src] = 1

        tgt = edge.target()
        if(target_dict[tgt] != 0):
            return False
        target_dict[tgt] = 1
    return True

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

def write_subterms(subgraphs):
    count_path = RESULT_PATH.replace('{0}', 'subterms_count.csv')
    shrink_path = RESULT_PATH.replace('{0}', 'subterms_shrink_power.csv')

    with open(count_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'count'])
        # Write each row separately to a CSV file
        for _, subg_details in sorted(subgraphs.items(), key=lambda item: item[1]['count'], reverse=True):
            writer.writerow([subg_details['id'], subg_details['serialisation'], subg_details['count']])
    print(f'Subterm count has been saved to {count_path}.')
    with open(shrink_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for sub, subg_details in sorted(subgraphs.items(), key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])
    print(f'Shrinking power has been saved to {shrink_path}.')

    # Csv filters
    csv_filters_path = RESULT_PATH.replace('{0}', '/csv_filters')
    if not os.path.exists(csv_filters_path):
        os.makedirs(csv_filters_path)

    filtered_subgraphs = list(subgraphs.copy().items())

    print(filtered_subgraphs)

    # csv_file1: Write subterms of size 1
    temp_collection = []
    with open(f'{csv_filters_path}/1_filter_size_1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for idx, filtered_subgraph in reversed(list(enumerate(filtered_subgraphs))):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            if(len([v for v in sub.vertices()]) == 1):
                temp_collection.append((sub, subg_details))
                del filtered_subgraphs[idx]
        for sub, subg_details in sorted(temp_collection, key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])
    print(f'CSV size=1 filter applied.')

    # csv_file2: Write subterms of count 1
    temp_collection = []
    with open(f'{csv_filters_path}/2_filter_count_1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for idx, filtered_subgraph in reversed(list(enumerate(filtered_subgraphs))):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            if(subg_details['count'] == 1):
                temp_collection.append((sub, subg_details))
                del filtered_subgraphs[idx]
        for sub, subg_details in sorted(temp_collection, key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])

    print(f'CSV count=1 filter applied.')

    # csv_file3: Write subterms of count 2
    temp_collection = []
    with open(f'{csv_filters_path}/3_filter_count_2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for idx, filtered_subgraph in reversed(list(enumerate(filtered_subgraphs))):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            if(subg_details['count'] == 2):
                temp_collection.append((sub, subg_details))
                del filtered_subgraphs[idx]
        for sub, subg_details in sorted(temp_collection, key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])
    print(f'CSV count=2 filter applied.')

    # csv_file4: Write subterms of only unary operations
    temp_collection = []
    with open(f'{csv_filters_path}/4_filter_only_unary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for idx, filtered_subgraph in reversed(list(enumerate(filtered_subgraphs))):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            if(is_only_unary_operations(sub)):
                temp_collection.append((sub, subg_details))
                del filtered_subgraphs[idx]
        for sub, subg_details in sorted(temp_collection, key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])
    print(f'CSV only unary filter applied.')

    # csv_file5: Write subterms of top unary 
    temp_collection = []
    with open(f'{csv_filters_path}/5_filter_top_unary.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for idx, filtered_subgraph in reversed(list(enumerate(filtered_subgraphs))):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            if(len(subg_details['serialisation']) == 2):
                temp_collection.append((sub, subg_details))
                del filtered_subgraphs[idx]
        for sub, subg_details in sorted(temp_collection, key=lambda item: item[1]['shrinking_power'], reverse=True):
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])
    print(f'CSV top unary filter applied.')

    # csv_file6: Write rest subterms
    with open(f'{csv_filters_path}/6_rest.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['serialisation', 'size', 'count', 'shrinking_power'])
        # Write each row separately to a CSV file
        for filtered_subgraph in sorted(filtered_subgraphs, key=lambda item: item[1]['shrinking_power'], reverse=True):
            sub = filtered_subgraph[0]
            subg_details = filtered_subgraph[1]
            writer.writerow([subg_details['serialisation'], len([v for v in sub.vertices()]), subg_details['count'], subg_details['shrinking_power']])