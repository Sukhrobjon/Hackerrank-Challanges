# Create a function that takes a list
# Create an empty list
# Iterate through the old list
# Get the last index of the old list
# Append to the new list
# Return the new list
# Shiv Toolsidass

'''

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

a b c
  d
e f g

-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
 
-63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18

0 4 3
  1
8 6 6
'''

example_list = [0, 1, 2, 3]


def reverse_list(old_list):
    new_list = []

    for index in range(len(old_list)):
        new_index = len(old_list) - 1 - index
        new_list.append(old_list[new_index])
    return new_list


print(reverse_list(example_list))


#
# Your previous Python 2 content is preserved below:
#
# def say_hello():
#     print 'Hello, World'
#
# for i in xrange(5):
#     say_hello()
#
#
# #
# # Your previous Plain Text content is preserved below:
# #
# # '''
# #  Given a list, return a reversed version of the list.
# #
# #  [1,2,3,4,5]
# #  [5,4,3,2,1]
# #
# #
# # '''
# #
#
