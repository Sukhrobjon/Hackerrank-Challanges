def strong_password(n, password):
    """
    Function checks if password is strong enough to meet following requirements
    - Its length is at least 6.
    - It contains at least one digit.
    - It contains at least one lowercase English character.
    - It contains at least one uppercase English character.
    - It contains at least one special character("!@#$%^&*()-+").
    """
    required_chars = 0
    # check for lowercase
    lower_case = any(char.islower() for char in password)
    upper_case = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_case = any(char for char in password if char in "!@#$%^&*()-+")
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
    # final check for length after required chars added
    if (required_chars + n) > 5:
        required_chars = required_chars
    else:
        required_chars = 6 - (required_chars + n) + required_chars

    return required_chars
n = 6
password = ''
output = 3
print(strong_password(0, password))

failing_case = """5, jnhqj, output = 3"""
