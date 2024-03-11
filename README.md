# FRET Macrofication Project

The project's aim is to create a tool to find repeating patterns in formal languages. The use case used to model the tool are NASA's FRET requirements. Ideally, after having found repeated patterns that would allow for the construction of macros. 

To use the software you need a .json of formulas in a formal language of your choice, that would:
- be serialised using prefix notation, and then
- analysed for isomorphic subgraphs

## Running the software
Run the main.py script in /src by passing it the .json file of requirements you need to serialise.

Example run from fret-macrofication/FRET/src: `python3 .\main.py ..\..\data\fret_data\raw\UseCase6.json`

## Running steps separately
Keep in mind the output paths will need to be changed as this is not the intended way to run the software!

### Serialisation
Run the main.py script in /src/serialisation by passing it the .json file of requirements you need to serialise.

Example run from fret-macrofication/FRET/serialisation/src: `python3 .\main.py ..\data\fret_data\raw\UseCase6.json`

### Isomorphism
Run the main.py script in /src/isomorphism after the output of the previous section is constructed.

Example run from fret-macrofication/FRET/isomorphism/src: `python3 .\main.py`
