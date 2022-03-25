# cleanString.py: to make this list of strings uniform and
# ready for analysis: stripping whitespace, removing punctuation symbols, and standardizing
# on proper capitalization.


import re


def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result