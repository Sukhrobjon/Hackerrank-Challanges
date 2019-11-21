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
    counter = Counter(text)
    print(f'before sort: {counter}')
    counter = sorted(counter.items(), key=lambda kv: -kv[1])
    print(f'after sort: {counter}')

    for i in range(len(counter)):
        pair_1 = counter[i]
        pair_2 = counter[i+1]
        if abs(pair_1[1] - pair_2[1]) <= 1:
            pair = (pair_1[0], pair_2[0])
            # check if char is not consecutive in the text
            if not _is_consecutive()
                print(pair_1, pair_2)
                return (pair_1[1] + pair_2[1])

    return 0


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


text = "asdcbsdcagfsdbgdfanfghbsfdab"
two_alternating_chars(text)
