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


def capitalized_words(arr):
    capitalized = []

    for word in arr:
        if word[0].isupper():
            capitalized.append(word)

    return capitalized
a = ['APp and', 'Python', 'javascpript']
print(capitalized_words(a))