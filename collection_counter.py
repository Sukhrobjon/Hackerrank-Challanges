# shoe_number = int(input("number of shoes: "))

# all_sizes = [int(size) for size in input("size: ").split()]
# print(all_sizes)
num_customers = int(input("number of customer: "))
wanted = {k: v for k, v in (input().split() for _ in range(num_customers))}
key, value = input().split()
print(wanted)
