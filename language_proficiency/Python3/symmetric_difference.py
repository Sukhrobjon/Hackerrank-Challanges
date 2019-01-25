def sym_diff(a ,b):
    diff = sorted(list(a.symmetric_difference(b)))
    
    return diff


m = int(input())
a = set([int(x) for x in input().split()])
n = int(input())
b = set([int(x) for x in input().split()])
print(sym_diff(a, b))
