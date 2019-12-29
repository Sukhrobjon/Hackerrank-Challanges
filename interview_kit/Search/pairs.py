def pairs(k, numbers):
    """
    Determine the number of pairs that have difference equal to k
    Args:
        array(int): list of integers
        k(int): difference between two element needs be found
    Note: k is assumed to be positive
    """

    count = 0
    elems = []
    for i in range(len(numbers)-1):
        curr = numbers[i]
        print(curr)
        for j in range(i+1, len(numbers)):
            # to make sure the difference is positive
            # it helps to eleminate some cases beforehand
            # if curr < numbers[j]:
            if abs(numbers[j] - curr) == k:
                elems.append(([numbers[j], curr]))
                count += 1
    
    return count


numbers = [1, 5, 3, 4, 2]
k = 2
result = pairs(k, numbers)
print(result)

