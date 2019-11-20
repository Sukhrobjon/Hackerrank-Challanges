def strong_password(n, password):
    if n < 6:
        return 6 - n
    required_chars = 0
    # check for lowercase
    lower_case = any(char.islower() for char in password)
    upper_case = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_case = any(char for char in password if char in '"!@#$%^&*()-+"')
    if lower_case is False:
        print('lowercase')
        required_chars += 1
    if upper_case is False:
        print('uppercase')
        required_chars += 1
    if digit is False:
        print('digit')
        required_chars += 1
    if special_case is False:
        print('special case')
        required_chars += 1
    return required_chars

n = 6
password = 'aaaaaa'
print(strong_password(n, password))

failing_case = """5, jnhqj"""

    
    
