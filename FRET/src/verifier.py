import json

def breakDown(expr):
    if(type(expr) == list):
        if(len(expr) == 2):
            # if(expr[0] == '!'):
            #     return f'{breakDown(expr[0])}({breakDown(expr[1])})'
            return f'({breakDown(expr[0])} {breakDown(expr[1])})'
        elif(len(expr) == 3):
            if(expr[0] == 'G' or expr[0] == 'F'):
                return f'({breakDown(expr[0])} {breakDown(expr[1])} {breakDown(expr[2])})'
            return f'({breakDown(expr[1])} {breakDown(expr[0])} {breakDown(expr[2])})'
    elif(type(expr) == str):
        return expr

def serialisedJSON2FRET(json_data):
    problemsOccurred = False
    for reqt in json_data:
        currReqt = reqt['ast']
        evaluated = (breakDown(currReqt))
        truth = reqt['fret']

        if(evaluated != truth):
            problemsOccurred = True
            print('Problems with ', reqt['id'])
            print(evaluated)
            print(truth)
            break
    if(not problemsOccurred):
        print('All translations verified!')
    

with open('C:/Users/klouc/Desktop/fret-macrofication/FRET/src/FRET2JSON/serialised_fret.json', 'r') as file:
    # Load JSON data from the file
    data = json.load(file)
    serialisedJSON2FRET(data)
