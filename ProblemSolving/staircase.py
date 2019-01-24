def staircase(n):
    return ('\n'.join([' '*(n-i) + '#'*i for i in range(1, n+1)]))

print(staircase(4))


