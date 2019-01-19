from collections import Counter

def sock_merchant(num_socks, arr):
    """return an integer representing the number 
    of matching pairs of socks that are available.
    """
    sock_dict = Counter(arr)
    print(sock_dict)
    value_list = list(sock_dict.values())
    pairs = 0
    for val in value_list:
        if val >= 2:
            if val % 2 == 0:
                pairs += val
            else:
                pairs += val - 1
    print(pairs)
    return pairs // 2


socks = "44 55 11 15 4 72 26 91 80 14 43 78 70 75 36 83 78 91 17 17 54 65 60 21 58 98 87 45 75 97 81 18 51 43 84 54 66 10 44 45 23 38 22 44 65 9 78 42 100 94 58 5 11 69 26 20 19 64 64 93 60 96 10 10 39 94 15 4 3 10 1 77 48 74 20 12 83 97 5 82 43 15 86 5 35 63 24 53 27 87 45 38 34 7 48 24 100 14 80 54"
arr_socks = socks.split()
arr_socks = [int(i) for i in arr_socks]
num_socks = 7
print(arr_socks)
arr = [1, 2, 1, 2, 1, 2, 3]
print(sock_merchant(7, arr_socks))
