import pdb
from collections import defaultdict
def most_frequent_char(s):
    frequent_characters = defaultdict(dict)
    max_character = ''
    idx = 0
    while idx < len(s):
        # pdb.set_trace()
        if s[idx] not in frequent_characters:
            frequent_characters[s[idx]]["count"] = 0
            frequent_characters[s[idx]]["count"] += 1
            frequent_characters[s[idx]]["idx"] = idx
        else:
            frequent_characters[s[idx]]["count"] += 1
        max_character = get_most_freq_char(frequent_characters, s[idx], max_character)
        idx += 1

    return max_character
  

def get_most_freq_char(d, current, max_character):
    # pdb.set_trace()
    if max_character == '':
        return current
    
    if d[current]["count"] > d[max_character]["count"]:
        return current
    if d[current]["count"] < d[max_character]["count"]:
        return max_character
    if d[current]["count"] == d[max_character]["count"] and d[current]["idx"] > d[max_character]["idx"]:
        return max_character
    else:
        return current
    

print(most_frequent_char('bookeeper'))