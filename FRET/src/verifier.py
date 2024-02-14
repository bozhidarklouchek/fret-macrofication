import json, sys
from fret_serialiser import fret2json

def json2fret(expr):
    if(type(expr) == list):
        if(len(expr) == 2):
            if(type(json2fret(expr[1])) == str):
                return f'({json2fret(expr[0])} {json2fret(expr[1])})'
            else:
                return f'({json2fret(expr[0])} ({json2fret(expr[1])}))'
        elif(len(expr) == 3):
            if(expr[0] == 'G' or expr[0] == 'F'):
                if(type(json2fret(expr[2])) == str):
                    return f'({json2fret(expr[0])} {json2fret(expr[1])} {json2fret(expr[2])})'
                else:
                    return f'({json2fret(expr[0])} {json2fret(expr[1])} ({json2fret(expr[2])}))'
            else:
                if(type(json2fret(expr[1])) == str and type(json2fret(expr[2])) == str):
                    return f'({json2fret(expr[1])} {json2fret(expr[0])} {json2fret(expr[2])})'
                elif(type(json2fret(expr[1])) == str):
                    return f'({json2fret(expr[1])} {json2fret(expr[0])} ({json2fret(expr[2])}))'
                elif(type(json2fret(expr[2])) == str):
                    return f'(({json2fret(expr[1])}) {json2fret(expr[0])} {json2fret(expr[2])})'
                else:
                    return f'(({json2fret(expr[1])}) {json2fret(expr[0])} ({json2fret(expr[2])}))'
    elif(type(expr) == str):
        return expr

def verify_serilisations(reqts, serialisedFormulasCount):
    print('Verifying serilisations...')
    for reqt in reqts:
        evalFret = json2fret(reqt['serialisation'])
        reqt['evaluatedFret'] = evalFret
        reqt['evaluatedSerialisation'] = fret2json(reqt['reqid'], evalFret)

    successfulSerilisations = 0
    for reqt in reqts:
        if(reqt['serialisation'] == reqt['evaluatedSerialisation'] and reqt['serialisation'] != None):
             successfulSerilisations += 1
        elif(reqt['serialisation'] != reqt['evaluatedSerialisation']):
            print('Problems with the serialisation of', reqt['reqid'])

    print(f'Verified {successfulSerilisations}/{serialisedFormulasCount}.', end=' ')
    if(successfulSerilisations == serialisedFormulasCount):
        print('Hooray :)')
    
# with open(sys.argv[1], 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     verify(data)
