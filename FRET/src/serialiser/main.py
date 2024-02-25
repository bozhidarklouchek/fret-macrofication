from fret_reader import getReqts
from fret_serialiser import addSerilisationToReqts
from verifier import verify_serilisations
from pathlib import Path
import sys, json, csv

SAVE_RESULT = True

reqts, readFormulasCount = getReqts(sys.argv[1])
if(len(reqts) != 0):
    reqts_with_serilisations, serialisedFormulasCount = addSerilisationToReqts(reqts, readFormulasCount)
    verify_serilisations(reqts_with_serilisations, serialisedFormulasCount)
    if(SAVE_RESULT):
        result = [{k : v for k,v in reqt.items() if k != 'evaluatedSerialisation' and k != 'evaluatedFret'} for reqt in reqts_with_serilisations]
        Path("../../output").mkdir(parents=True, exist_ok=True)
        # Save to .json
        with open('../../output/serialisation.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        # Save to .csv
        with open('../../output/serialisation.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result[0].keys())
            for res in result:
                writer.writerow(res.values())
        print('Saved result!')
