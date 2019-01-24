
def plus_minus(arr):
    '''
    print out the ratio of positive, negative and zero 
    items in the array, each on a separate line rounded to six decimals.
    '''
    # number of all positive numbers in arr
    positive = len([x for x in arr if x > 0])
    # number of all negative numbers in arr
    negative = len([x for x in arr if x < 0])
    # number of zeros in arr
    zero = len([x for x in arr if x == 0])
    total = len(arr)
    precision = [positive, negative, zero]
    for i in precision:
        # prints out the float 6 decimal points even it ends with 0s
        print("{:.6f}".format(round(i/total, 6)))
    
arr = [-4, 3, -9, 0, 4, 1]
plus_minus(arr)
'''
Output :
0.500000
0.333333
0.166667
'''
