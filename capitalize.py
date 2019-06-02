'''
Print the capitalized string, .

Sample Input

chris alan

Sample Output

Chris Alan
'''
def solve(s):
    l = list(s)
    l[0] = l[0].upper()
    for i in range(len(l)):
        if(l[i] == ' '):
            l[i+1] = l[i+1].upper()
    s = ''.join(l)
    return s

if __name__ == '__main__':
    name = 'chris alan'
    print(name.title())
    # print(solve(name))
