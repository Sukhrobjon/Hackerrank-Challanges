def count_swaps(arr):
    """
        Sorts the array with bubble sort algorithm
        and returns number of swaps made to sort the array
    """
    count = 0
    swapped = False
    while swapped is not True:
        swapped = True
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                swapped = False

        print(arr)
    # return count
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[len(arr) - 1]))



arr = [5, 2, 4, 1, 3]
(count_swaps(arr))
