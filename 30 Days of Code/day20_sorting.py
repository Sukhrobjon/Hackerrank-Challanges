import time
def optimized_bubble_sort(arr):
    """
        Sorts the array with bubble sort algorithm
        and returns number of swaps made to sort the array
    """
    count = 0
    swapped = False
    while(swapped != True):
        swapped = True
        for j in range(len(arr)-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
                swapped = False

    print(arr)
    return count

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
if __name__ == "__main__":
    start_time = time.time()
    arr = [4, 1, 3, 5, 2]
    sorted_arr = [x for x in range(10000)]
    print(optimized_bubble_sort(sorted_arr))
    # print(sorted_arr)
    print(f"----{time.time() - start_time} seconds-----")
