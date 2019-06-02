'''
    You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
    without any duplicates. You are allowed to swap any two elements. You need to find the 
    minimum number of swaps required to sort the array in ascending order.
    For example, [7, 1, 3, 2, 4, 5, 6] given the array  we perform the following steps:

    i   arr                     swap (indices)
    0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
    1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
    2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
    3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
    4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
    5   [1, 2, 3, 4, 5, 6, 7]

    it took 5 steps to sort the array 
'''

# def minumum_swaps_to_sort(array):
#     '''
#         Takes unordered array consisting of consecutive integers
#         and return the number of swap taken to sort the array
#     '''
#     # min_index = 0
#     # shift = 0 # shift to the right
#     sorted_array = sorted(array) 
#     num_swaps = 0
#     for index, value in enumerate(array):
#         # find the index of min number
#         correct_value = index + 1
        
#         min_value_index = find_index_of_min_number(array)
#         if correct_value != value:
#             # swap the value with right index
#             # to_swap_index = find_index_of_min_number(array)
#             array[index], array[to_swap_index] = array[to_swap_index], array[index]
#             num_swaps += 1
        
#             print('minnum: ', array[min_value_index])
    
            
#     print(array)
#     return num_swaps

def selection_sort(array):
    
    count = 0
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
                count += 1


        array[i], array[min_index] = array[min_index], array[i]
    print('swap: ', count - 1)
    return array

def find_index_of_min_number(array):
    ''' Takes an array and returns the index of the first minimum number in the array'''
    min_index = 0
    for index, value in enumerate(array):
        if value < array[min_index]:
            min_index = index
    return min_index


def swap(a, b):
    a, b = b, a

array = [7, 1, 3, 2, 4, 5, 6]  
arr = [4, 3, 1, 2]
arr_3 = [2, 3, 4, 1, 5]

# print("Shoud return 3: ", minumum_swaps_to_sort(array))

print(selection_sort(arr_3))


def minimum_swaps(arr):
    sorted_arr = sorted(arr)
    index_dict = {value: index for index, value in enumerate(arr)}
    swaps = 0

    for index, value in enumerate(arr):
        # get the correct value from sorted array
        correct_value = sorted_arr[index]
        # check if current value is at the right place by comparing correct value
        if value != correct_value:
            # get the correct index of correct value from dict
            correct_index = index_dict[correct_value]
            # swap those values
            arr[correct_index], arr[index] = arr[index], arr[correct_index]
            index_dict[value] = correct_index
            index_dict[correct_value] = index
            # increment the number of swaps
            swaps += 1

    return swaps
