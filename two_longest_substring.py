def longest_substring(word):
    longest = 0
    counter = 0
    seen = set()
    start = 0
    index = 0
    # word = list(word)
    # while index < len(word) - 1:
    for char in word:
        print('index: ', char)
        # if word[index] not in seen:
        if char not in seen:
            seen.add(char)
            counter += 1
        # print(word[:counter])
        else:
        #     # if counter > longest:
        #     #     longest = counter
        #     # counter = 0
        #     # start += 1
            # index = start
            # print(word[:counter])
            break

    return counter

a = 'abcabcbb'
print(longest_substring(a))


    