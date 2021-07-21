def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        if (n * n) > num:
            return False
    return True

# Time Complexity - O(sqrt(n))
# Space Complexity = O(1) 