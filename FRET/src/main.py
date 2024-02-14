from fret_reader import getReqts
from fret_serialiser import addSerilisationToReqts
from verifier import verify_serilisations
import sys, json

SAVE_RESULT = True

reqts, readFormulasCount = getReqts(sys.argv[1])
if(len(reqts) != 0):
    reqts_with_serilisations, serialisedFormulasCount = addSerilisationToReqts(reqts, readFormulasCount)
    verify_serilisations(reqts_with_serilisations, serialisedFormulasCount)
    if(SAVE_RESULT):
        with open('C:/Users/klouc/Desktop/fret-macrofication/FRET/output/result.json', 'w', encoding='utf-8') as f:
            json.dump([{k : v for k,v in reqt.items() if k != 'evaluatedSerialisation' and k != 'evaluatedFret'} for reqt in reqts_with_serilisations], f, ensure_ascii=False, indent=4)
        print('Saved result!')
