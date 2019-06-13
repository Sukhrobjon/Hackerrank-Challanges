# follow what Alan has offered

'''
Ikey's solution for longest unique substring

def longest_unique_substring(str):
    longest = ""
    curr = ""

    for char in str:
        if char in curr:
            if len(curr) > len(longest):
                longest = curr

            index_of_dub = curr.index(char)
            curr = curr[index_of_dub + 1:]

        curr += char

    return longest

a = "abcabcbb"

print(longest_unique_substring(a))'''

def optimized_longest_substring(word):
    seen = {}
    index = starter = longest = counter = 0

    while index < len(word) - 1:
        
        cur_char = word[index]
        
        if cur_char in seen:    
            # update the left side of the window or new starter
    
            starter = seen[cur_char]
            seen[cur_char] = index + 1
            index = starter
            print("new index of dub char: ", seen[cur_char])
            print("starter: ", starter)
            counter = seen[cur_char] - starter
        
        seen[cur_char] = index + 1
        print('index: ', index)
        index += 1

        longest = max(counter, longest)
        print(seen)
    
    return longest

a = 'abcabcbb'
b = 'dvdf'
c = 'pwwkew'
print(optimized_longest_substring(b))






def capitalized_words(arr):
    capitalized = []

    for word in arr:
        if word[0].isupper():
            capitalized.append(word)

    return capitalized
a = ['APp and', 'Python', 'javascpript']
# print(capitalized_words(a))

