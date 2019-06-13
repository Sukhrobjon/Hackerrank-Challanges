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
        
        if cur_char not in seen:    
            seen[cur_char] = index + 1
            print("index in if: ", index)
            index += 1
            

        else: # see the duplicate
            # print(cur_char)
            # before setting the new index of the char we need to shift the starter
            starter = seen[cur_char]
            
            # set the dublicated char's value with updated index
            seen[cur_char] = index + 1
            # updatet the counter
            counter = index - starter + 1
            print("counter: ", counter)
            print("starter: {}, index: {}".format(starter, index))
            # reset the index to start at the starter
            index = starter
            print("index after new starter: ", index)
            
            
        longest = max(counter, longest)
        print("longest: ",longest)
        print(seen)
    return longest


a = 'abcabcbb'
b = 'dvdf'
print(optimized_longest_substring(b))






def capitalized_words(arr):
    capitalized = []

    for word in arr:
        if word[0].isupper():
            capitalized.append(word)

    return capitalized
a = ['APp and', 'Python', 'javascpript']
# print(capitalized_words(a))

