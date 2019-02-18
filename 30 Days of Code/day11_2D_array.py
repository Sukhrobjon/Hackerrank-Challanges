arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0]]


def hour_glass(arr):
    """
        Calculate the hourglass sum for every hourglass in list,
        then return the maximum hourglass sum
    """
    result = []
    for column in range(4):
        for row in range(4):
            row_1 = sum(arr[column][row:row+3])
            row_2 = arr[column+1][row+1]
            row_3 = sum(arr[column+2][row:row+3])
            total = row_1 + row_2 + row_3
            result.append(total)
    print(result)
    return max(result)

print(hour_glass(arr))
