from itertools import groupby

def compress_string(input_str):
    """ takes string input and groups by number of occurence using
        using groupby() builtin 
        Returns a list of tuple of (count, item) 
    """
    group_items = [k for k, g in groupby(input_str)]  # returns only the items
    group_list = [list(g) for k, g in groupby(input_str)]  # returns list of items

    pairs = []
    for i in range(len(group_list)):
        count = len(group_list[i])
        item = int(group_items[i])
        a = (count, item)
        pairs.append(a)
    return pairs
    

number = '1222311'
print(*compress_string(number))
"""
    # one solution
    from itertools import groupby
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

"""
