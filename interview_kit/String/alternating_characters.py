def alternating_characters(word):
    word = list(word)
    deletion = 0
    for index in range(len(word) - 1):
        if word[index] == word[index+1]:
            # word.pop(index+1)
            deletion += 1
    # print(word)
    return deletion


word = 'aaaa'
word_2 = 'bababa'
print("Before: ", word)
word = alternating_characters(word_2)
print("Deletion: ", word)
