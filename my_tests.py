
print(len(set([str(input()) for x in range(int(input()))])))
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

# print(len(a.union(b)))
n = int(input("enter number between 1-20: "))
k = [x*x for x in range(1,n+1)]
# for i in range(1,6):
#     print(i*i)
print(*k, sep="\n")