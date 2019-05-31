# def find_max_bitwise_and(n, k):
#     # n = 5
#     # k = 2

#     # create the set of numbers from 1 to n
#     s = [int(num) for num in range(1, n+1)]
#     # print(s)
#     max_value = 0

#     for i in range(len(s)-1):
#         a = s[i]
#         print("a: ", a)
#         for j in range(len(s)):

#             if a < s[j]:
#                 val = a & s[j]
#                 print('val:', val)
#                 if val > max_value and val < k:
#                     max_value = val

#     # print('max_val: ', max_value)
#     return max_value

from itertools import permutations, combinations
n = 5
k = 2
# Get all permutations of length 2
# and length 2
s = [int(num) for num in range(1, n+1)]
perm = permutations(s, 2)

# Print the obtained permutations
# for pair in list(perm):
#     print(pair[0])

comb = combinations(s, 2)

# Print the obtained combinations
# result = []
max_value = 0

for pair in list(comb):
    # print(pair)
    num = pair[0]&pair[1]
    if num > max_value and num < k:
        max_value = num
        # result.append(num)

print(max_value)


# ==========================================


