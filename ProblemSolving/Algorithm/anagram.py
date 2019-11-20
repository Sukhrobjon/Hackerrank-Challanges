def min_num_to_anagram(text):
    
    if len(text) % 2 != 0:
        return -1
 
    str_1 = text[:len(text)//2]
    str_2 = text[len(text)//2:]
    count_1 = [0] * 26
    count_2 = [0] * 26
    offset = 97
    
    for i in range(len(str_1)):
        count_1[ord(str_1[i]) - offset] += 1
        count_2[ord(str_2[i]) - offset] += 1
    
    return count_1, count_2

    
text = "xabbbx"
print(min_num_to_anagram(text))