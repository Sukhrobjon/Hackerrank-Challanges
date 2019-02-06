# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict


ordered_dict = OrderedDict()
n = int(input())
for data in range(n):
    data = input().split()
    key = " ".join(data[:-1])
    value = int(data[-1])
    if key in ordered_dict:
        ordered_dict[key] += value
    else:
        ordered_dict[key] = value

for key, value in ordered_dict.items():
    print("{} {}".format(key, value))
