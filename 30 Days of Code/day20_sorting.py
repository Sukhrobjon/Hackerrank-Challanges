def bubble_sort(arr):
    """
        Sorts the array with bubble sort algorithm
        and returns number of swaps made to sort the array
    """
    count = 0
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1

    print(arr)
    return count


arr = [4, 1, 3, 5, 2]
print(bubble_sort(arr))
