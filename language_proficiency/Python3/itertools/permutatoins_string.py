from itertools import permutations

word, num = input().split()

word_perm = permutations(list(word.upper()), int(num))
sorted_perm = sorted(list(word_perm))
for i in sorted_perm:
    print(",".join(i))
# print(sorted_perm)

# word = "hello"

# word_list = list(word)
# print(word_list)