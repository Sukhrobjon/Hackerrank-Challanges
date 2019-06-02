def min_max_sum(arr):
    total = sum(arr)
    print((total - max(arr)), total - min(arr))

arr = [1, 2, 3, 4, 5]
min_max_sum(arr)