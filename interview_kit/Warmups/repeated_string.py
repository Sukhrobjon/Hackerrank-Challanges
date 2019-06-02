def repeated_string(s, n):
    s = (s * (n//len(s) + 1))[:n]
    return s.count('a')

""" 
create a new list add the each item until the length is equal to number

"""
s = 'aba'
n = 100
print(repeated_string(s, n))