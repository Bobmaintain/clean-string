# cleanString3.py: to make this list of strings uniform and
# ready for analysis: stripping whitespace, removing punctuation symbols, and standardizing
# on proper capitalization.


for x in map(remove_punctuation, states):
    print(x)