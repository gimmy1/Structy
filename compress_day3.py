def compress(s):
    idx, jdx = 0, 0
    result = []
    while jdx < len(s):
        if s[jdx] != s[idx]:
            difference = jdx - idx
            if difference == 1:
                difference = ''
            result.append(f"{str(difference)}{s[idx]}")
            idx = jdx
        jdx += 1
    difference = jdx - idx
    if difference == 1:
        difference = ''
    result.append(f"{str(difference)}{s[idx]}")
    return ''.join(result)

print(compress('ccaaatsss')) # -> '2c3at3s' 2c3a1t3s