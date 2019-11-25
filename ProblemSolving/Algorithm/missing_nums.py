def missing_numbers(arr, brr):
    missing = set()
    i, j = 0, 0
    while i < len(arr) and j < len(brr):
        # if nums are equal just move to next
        print(f"i: {i}, j: {j}")
        if arr[i] == brr[j]:
            i += 1
            j += 1
        else:
            missing.add(brr[j])
            j += 1
    # check if we check all items in the bigger list
    if j != len(brr):
        # add the rest of the missing number at the end of the
        # bigger list
        for j in range(j, len(brr)):
            missing.add(brr[j])

    return missing


def missing_numbers_v2(arr, brr):
    from collections import Counter
    counter_a = Counter(arr)
    counter_b = Counter(brr)
    missing_nums = []
    for key, _ in counter_b.items():
        if key not in counter_a or counter_a[key] != counter_b[key]:
            missing_nums.append(key)
    
    return sorted(missing_nums)


arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
# arr = [2, 3, 4, 5]
# brr = [2, 3, 4, 5, 6, 5]
print(missing_numbers_v2(arr, brr))
