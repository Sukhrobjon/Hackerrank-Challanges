from itertools import product

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print(*list(product(a, b)))



# if "__name__" == "main":
    
#     cross_product
