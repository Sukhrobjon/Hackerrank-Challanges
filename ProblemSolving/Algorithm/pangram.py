def pangrams(s):
    # lowercase the string
    # create a 26 letter
    is_pangram = [0] * 26
    s = s.replace(" ", "").lower()
    for char in s:
        index = ord(char) - 97
        is_pangram[index] += 1
    for i in is_pangram:
        if i == 0:
            return "not pangram"
    return "pangram"
