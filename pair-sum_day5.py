from collections import defaultdict

def pair_sum(numbers, target_sum):
    indexes = defaultdict(int)
    for idx, num in enumerate(numbers):
        difference = target_sum - num
        if difference in indexes:
            return (indexes[difference], idx)
        indexes[num] = idx

print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2))