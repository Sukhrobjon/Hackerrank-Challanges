def compareTriplets(a, b):
    score = []
    a_score = b_score = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score += 1
    score = [a_score, b_score]
    return score


a = [5, 7, 7]
b = [3, 6, 10]
print(compareTriplets(a, b))
