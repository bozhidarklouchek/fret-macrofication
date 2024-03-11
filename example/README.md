# Example FRET Requirements

Here is a collection of FRET requirements. Inside each collection you will find several files:
- FRET JSON - the file containing the original FRET data
- requirements.csv - the extracted FRET requirements in the format:
  - requirement id,
  - the FRET formula, and
  - the JSON serialisation
- subterms.csv - all subterm found in the requirements in the format:
  - subterm id,
  - JSON serialisation of the subterm, and
  - the count of occurrece
- original.pdf - a graph where:
  - each vertex is a subterm (coloured so as the occurrence count grows, the colour gets colder, e.g., vertices with counts of 1-2 are generally red/yellow and the highest counts are generally blue/purple), and
  - each edge signifies that a target term is a subterm of a source term
- min_count_X.pdf - a graph that's the same as original.pdf, except that it only contains subterms with an occurrence count of X or more