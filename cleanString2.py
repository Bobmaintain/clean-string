# cleanString2.py: to make this list of strings uniform and
# ready for analysis: stripping whitespace, removing punctuation symbols, and standardizing
# on proper capitalization.
import re

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
    clean_ops = [str.strip, remove_punctuation, str.title]


def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result