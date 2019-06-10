def longest_substring(word):
    longest = 0
    counter = 0
    seen = []
    start = 0
    index = 0
    all_substring = []
    while index <  len(word):
        # print('index: ', char)
        print("seen: ",seen)
        if word[index] not in seen:
            print("inside if")
            seen.append(word[index])

            counter += 1
            print("current char: ",word[index])
            print("index: ", index)
            index += 1
            
        
        else: # repeated char found
            print("else")
            # break
            all_substring.append(list(seen))
            if counter > longest: # check if current substring is longest
                longest = counter
                print("counter: ", counter)
            counter = 0 # reset the counter
            start += 1 # shift the pointer to the next char 
            index = start # reset the index at the beginning of new substring
            print("index in else:", index)
            all_combos = list(seen)
            print("combo: ", all_combos)
            seen = [] # reset the set for new possible substring 
            # print(word[:counter])
        print('last set:', seen)
        # index += 1
    print(all_substring)
    return longest

# i = 0
# while i < 9:
#     print("i: ", i)
#     i += 1


a = 'pwwkew'
b = 'abcabcbb'
c = 'bbbbb'
print(longest_substring(a))


    
