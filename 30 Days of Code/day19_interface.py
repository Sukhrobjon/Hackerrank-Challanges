import math

def divisor_sum(number):
    """
       Return the sum of the all divisor of given number 
       Run time O(n), space O(1)
    """
    divisors = []
    for i in range(1, number+1):
        if(number % i == 0):
            divisors.append(i)
    return sum(divisors)

def optimized_divisor_sum(number):
    """
       Return the sum of the all divisor of given number 
       Run time O(sqrt(n)), space O(1)
    """
    divisors = []
    i = 1
    while i <= math.sqrt(number):
        if(number % i == 0):
            if number // i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number//i)
        i += 1
    divisors = sorted(divisors)
    return divisors

print(optimized_divisor_sum(100))
