import json, sys

KEY = 'ftInfAUExpanded'
OUTPUT_FILE_PATH = "FRET/tests/read_json.txt"

def readJson(file_path):
    print('Reading JSON data from', file_path, '...')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON file '{file_path}'.")
        return None
    
def extractFretFromKeyInJson(jsonData, key):
    reqts = list()
    if jsonData:
        for d in jsonData:
            # If semantics key present
            if(key in d['semantics'].keys()):
                reqts.append({'reqid': d['reqid'], 'fret': d['semantics'][key]})
            else:
                reqts.append({'reqid': d['reqid'], 'fret': None})

    # # Save to .txt
    # with open(OUTPUT_FILE_PATH, 'w') as file:
    #     for value in list(frets):
    #         file.write(value + '\n')
                
    readFormulasCount = len([reqt['fret'] for reqt in reqts if reqt['fret'] != None])          
    print(f'Read {len(reqts)} requirements with {readFormulasCount}/{len(reqts)} of them having included formulas.', end=' ')
    
    if(readFormulasCount == 0):
        print('So I am ending prematurely :(')
        sys.exit()
    return reqts, readFormulasCount

def getReqts(jsonPath):
    jsonData = readJson(jsonPath)
    frets = extractFretFromKeyInJson(jsonData, KEY)
    return frets

