def pairs_naive(k, numbers):
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


def pairs_optimized(k, numbers):
    """
    Determine the number of pairs that have difference equal to k
    Args:
        array(int): list of integers
        k(int): difference between two element needs be found
    Returns:
        pairs(int): number of pairs that their difference equal to k

    Note: k is assumed to be positive
    """
    # create a dict elements are keys indexes are value
    num_dict = {k: v for v, k in enumerate(numbers)}
    count = 0
    pairs = []
    for index, num in enumerate(num_dict.keys()):
        other_num = num + k
        if other_num in num_dict and num_dict[other_num] != index:
            count += 1
            pairs.append((other_num, num))
    # print(num_dict)
    return pairs


numbers = [1, 5, 3, 4, 2, 2]
k = 2
# result = pairs(k, numbers)
result = pairs_optimized(k, numbers)
print(result)

