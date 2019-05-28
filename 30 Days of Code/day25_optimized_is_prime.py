# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def is_prime(n):
    """
        Takes a single integer and return true if integer is prime, False otherwise
        Runtime: O(sqrt(n)) 
    """
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for divisor in range(2, 1 + max_divisor):
        if n % divisor == 0:
            return False
    return True


iteration = int(input())
test_cases = []
for i in range(iteration):
    test_cases.append(int(input()))

for i in test_cases:
    if is_prime(i):
        print("Prime")
    else:
        print("Not prime")
