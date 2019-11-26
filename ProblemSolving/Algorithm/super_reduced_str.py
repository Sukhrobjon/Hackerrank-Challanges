def reduced_str(text):
    """
    Return the super reduced string or `Empty String` if the final string is
    empty. For instance, the string aab could be shortened to b in one
    operation.
    """
    # reduced_str = ""
    # i = 0
    
    # while i < len(text) - 1:
    #     # if adjecents are equal skip(delete) them
    #     if text[i] == text[i+1]:
    #         i += 2
    #     else:
    #         reduced_str += text[i]
    #         i += 1
    #     print(f"i: {i}")
    # if not reduced_str:
    #     return f"Empty string"
    list_text = list(text)
    red = ""
    # return reduced_str
    i = len(list_text) - 1
    while i > 0:
        print("i:", i)
        if list_text[i] == list_text[i-1]:
            list_text.pop(i)
            list_text.pop(i-1)
            # i -= 2
            i = len(list_text) - 1
        else:
            red += str(list_text[i])
            i -= 1
        print(list_text)
        print("red:", red)
    return list_text


text = "aaabccddd"
print(reduced_str(text))
