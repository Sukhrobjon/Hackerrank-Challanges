# lets use counter
# create histogram for each list 
# check if the word in note is not in magazine
# return false
# if the word in note exist in magazine 
#   check if the number of word is equal 
#       print 'yes' 

from collections import Counter
def check_magazine(magazine, note):
    '''
        NOTE: The result of counters' operator substraction is a counter that shows 
        how many more values magazine is missing to match those present in note. 
        When an empty dict is returned, every element in note is present enough 
        times in magazine.


    '''
    magazine = Counter(magazine)
    note = Counter(note)

    # for word in note:
    #     if word not in magazine:
    #         return 'No'
    #     else:
    #         if note[word] != magazine[word]:
    #             return 'No'
    #         else:
    #             return 'Yes'
    
    if note - magazine == {}:
        print('Yes')
    else:
        print('No')

