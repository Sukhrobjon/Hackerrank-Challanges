
_, n = int(input()), input().split()
print(all([int(x) > 0 for x in n]) and any([i==i[::-1] for i in n]))
