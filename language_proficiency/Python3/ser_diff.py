m = int(input())
a = set([int(x) for x in input().split()])
n = int(input())
b = set([int(x) for x in input().split()])
diff = len(list(a.symmetric_difference(b)))
print(diff)