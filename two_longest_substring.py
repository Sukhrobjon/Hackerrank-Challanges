def longest_substring(word):
    longest = 0
    counter = 0
    seen = set()
    start = 0
    index = 0
    
    while(index < (len(word) - 1)):
        # print('index: ', char)
        print(seen)
        if word[index] not in seen:
            print("inside if")
            seen.add(word[index])

            counter += 1
            print(word[index])
        else:
            break
        #     # if counter > longest:
        #     #     longest = counter
        #     # counter = 0
        #     # start += 1
            # index = start
            # print(word[:counter])
            

    return counter

# i = 0
# while i < 9:
#     print("i: ", i)
#     i += 1

a = 'ihb'
print(longest_substring(a))


    
