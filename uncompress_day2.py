def uncompress(string):
    result = []
    idx = 0
    jdx = 0
    while jdx < len(string):
        if string[jdx].isalpha():
            result.append(int(string[idx:jdx]) * string[jdx])
            idx = jdx + 1
        jdx += 1
    return ''.join(result)

print(uncompress("2zc3"))

# NOTE: string concatenation in Python is a linear time because Python will copy the string to create a new string
# Based on your developed algorithm - you may use a Python list and join to return values.

# Time Complexity: O(nm) n is the number of groups m is the maximal number associated with any group
# Space Complexity: O(nm) string that is being constructed