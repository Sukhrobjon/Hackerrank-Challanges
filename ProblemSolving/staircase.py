def staircase(n):
    '''
    Print a staircase of size  using # symbols and spaces.
       #
      ##
     ###
    ####
    when n = 4
    '''
    return ('\n'.join([' '*(n-i) + '#'*i for i in range(1, n+1)]))

print(staircase(4))


