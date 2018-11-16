def swap_cases(s):
    new_s = list(s)
    for index, item in enumerate(new_s):
        new_s[index] = item.upper() if item.islower() else item.lower()
    # Convert list back to string
    return ''.join(new_s)


s = 'HackerRank.com presents "Pythonist 2".'
print(swap_cases(s))
