def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)




def is_palindrome(s):
    # return s == s[::-1]
    right = len(s) - 1
    for i in range(len(s)):
        if s[i] != s[right - i]:
            return False
        
    return True


n = 3
print(f"Result: {factorial(n)}")

s = "ba"
print(f"{s} is {is_palindrome(s)}")
