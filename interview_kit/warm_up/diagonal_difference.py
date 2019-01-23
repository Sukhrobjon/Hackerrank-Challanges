
def diagonal_difference(arr):
    """
    Takes square matrix 
    Return absolute difference between the sums of its diagonals.
    """
    # diag1 top-left to bottom-right
    diag1 = [row[i] for i, row in enumerate(arr)]
    # diag2 top-right to bottom-left
    diag2 = [row[-i-1] for i, row in enumerate(arr)]
    return abs(sum(diag1)- sum(diag2))


arr = [[11, 2, 4],
        [4,  5,  6], 
        [10, 8, -12]]

print(diagonal_difference(arr))


