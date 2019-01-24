def time_conversion24(s):
    '''
    Converts 12-hour AM/PM time to 24 hour format
    '''
    
    if s[-2:] == "AM" and s[:2] == "12":
        s = '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        print('before', s)
        s = s[:-2]
        print('after', s)
    # remove AM
    elif s[-2:] == 'AM':
        s = s[:-2]
    else:
        s = str(int(s[:2]) + 12) + s[2:-2]
    return s
    

s = '12:00:00AM'


print("In 12-hour format: ", s)
print("after 24 hour format: ", time_conversion24(s))

'''
Output
In 12-hour format:  12:00:00AM
after 24 hour format:  00:00:00
'''
