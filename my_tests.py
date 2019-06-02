
# print(len(set([str(input()) for x in range(int(input()))])))
# a = set([int(i) for i in input().split()])
# b = set([int(i) for i in input().split()])

# # print(len(a.union(b)))
# n = int(input("enter number between 1-20: "))
# k = [x*x for x in range(1,n+1)]
# # for i in range(1,6):
# #     print(i*i)
# print(*k, sep="\n")

# 2)**Single Number **
# Given an array of integers, every element appears twice except for one. Find that single one.
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

from collections import Counter
arr = [1, 2, 4, 5, 1, 4, 5]

arr_d = Counter(arr)
print(arr_d)
print(min(arr_d.values()))