# def longest_substring(word):
#     longest = 0
#     counter = 0
#     seen = []
#     start = 0
#     index = 0
#     all_substring = []
#     while index <  len(word):
#         # print('index: ', char)
#         print("seen: ",seen)
#         if word[index] not in seen:
#             print("inside if")
#             seen.append(word[index])

#             counter += 1
#             print("current char: ",word[index])
#             print("index: ", index)
#             index += 1
            
        
#         else: # repeated char found
#             print("else")
#             # break
#             all_substring.append(list(seen))
#             # if counter > longest: # check if current substring is longest
#             #     longest = counter
#             #     print("counter: ", counter)
#             counter = 0 # reset the counter
#             start += 1 # shift the pointer to the next char 
#             index = start # reset the index at the beginning of new substring
#             print("index in else:", index)
#             all_combos = (seen)
#             print("combo: ", all_combos)
#             seen = [] # reset the set for new possible substring 
#             # print(word[:counter])
#         print('last set:', seen)
#         # index += 1
#         if counter > longest:  # check if current substring is longest
#                 longest = counter
#                 print("COUNTER: ", counter)
#     print(all_substring)
#     return longest

# # i = 0
# # while i < 9:
# #     print("i: ", i)
# #     i += 1


# a = 'pwwkew'
# b = 'abcabcbb'
# c = 'bbbbb'
# sample = "c"
# print(longest_substring(sample))


class Solution(object):
    def lengthOfLongestSubstring(self, word):
    
        longest = index = counter = 0
        seen = set()

        while index < len(word) - 1:

            if word[index] not in seen:  # check if the char not in the list
                seen.add(word[index])
                counter += 1
                print("seen in if: ", seen)
            else:  # repeated char found
                print("seen before: ", seen)
                seen = set(word[index])  # empty the set and add the current char
                counter = 1 # and add one to counter bc there is one char in the set already
                print("seen after: ", seen)
            if counter > longest:  # check if current substring is longest
                    longest = counter
            index += 1
        return longest

   



a = 'abcabcbb'
b = 'pwwkew'
c = "dvdf"
obj = Solution()
print(obj.lengthOfLongestSubstring(a))


# def longest_substring(self, word):
   #     longest = 0
   #     seen = set()
#     counter = 0
#     for char in word:
#         if char not in seen:
#             seen.add(char)
#             counter += 1
#         else:
#             seen = set(char)
#             counter = 1

#         if counter > longest:
#             longest = counter

#     return longest
