"""
    Given a string, find the length of the longest 
    substring without repeating characters.
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3.
"""

def longest_substring(word):
    index = 0
    start = 0
    window = 1
    counter = 0
    seen = set()
    for char in word:
        if char not in seen:
            seen.add(char)
            counter += 1
    print('counter:', counter)
    window = counter - 1
    while index < len(word) - 1:
        cur_sub = word[index:index + window]
        print('current sub: ', cur_sub)
        if len(cur_sub) == len(set(cur_sub)):
            counter = len(cur_sub)
        # else:
        if counter > window:
            window = counter + 1
        # counter = 0
        start += 1
        index = start

    return window

a = 'pwwkew'
print(longest_substring(a))