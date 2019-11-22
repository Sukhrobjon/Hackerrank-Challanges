from collections import Counter


def two_alternating_chars(text):
    """
    you will be given a string. You must remove characters until the string is
    made up of any two alternating characters. When a character is chosen to
    remove, all instances of that character must be removed. it should create
    the longest string possible that contains just two alternating letters.
    E.g. s = abaacdabd => t = bdbd
    
    Returns:
        max_length(int): the maximum length of t for the given text, or 0 if
        not possible
    """
    max_len = 0
    counter = Counter(text)
    print(counter)
    # counter_list = counter.items()
    # print(counter_list)
    counter = sorted(counter.items())
    for i in range(len(counter)):
        for j in range(i+1, len(counter)):
            pair_1 = counter[i]
            pair_2 = counter[j]
            if abs(pair_1[1] - pair_2[1]) <= 1:
                pair = (pair_1[0], pair_2[0])
                cleaned_text = _keep_pair(pair, text)
                print(f"pairs: {pair}")
                print(f"cleaned text: {cleaned_text}, text: {text}")
                # check if char is not consecutive in the text
                if not _is_consecutive(cleaned_text):
                    if max_len < pair_1[1] + pair_2[1]:
                        # return (pair_1[1] + pair_2[1])
                        max_len = pair_1[1] + pair_2[1]

    return max_len


def _keep_pair(pair, text):
    """
    Alter the text to keep only chars the pair has
    """
    return ''.join(char for char in text if char in pair)


def _is_consecutive(altered_text):
    """Return true if there is consecutive char in the text"""
    for i in range(len(altered_text)-1):
        if altered_text[i] == altered_text[i+1]:
            return True
    return False


# print(_keep_pair('bd', 'abaacdabd'))
text = """muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz"""
print(two_alternating_chars(text))


# sample = [1, 2, 3, 4, 5, 6]
# for i in range(len(sample)):
#     for j in range(i+1, len(sample)):
#         print(f'i: {sample[i]}, j: {sample[j]}')

