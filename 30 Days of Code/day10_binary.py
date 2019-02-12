from itertools import groupby

def find_most_consecutive_ones(num):
    '''
         maximum number of consecutive 
    '''
    str_binary = ("{0:b}".format(num))
    binary_list = [list(g) for k, g in groupby(str_binary)]
    for _ in range(len(binary_list)):
        result = max(binary_list, key=len)
        if result[0] == '1':
            return len(result)
        else:
            binary_list.remove(result)
            continue
if __name__ == '__main__':
    n = 5
    print(find_most_consecutive_ones(n))