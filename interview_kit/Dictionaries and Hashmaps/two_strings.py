def twoStrings(s1, s2):
    # find intersection of two sets, since we need to find
    # at least one common char in both string
    is_common = set(s1).intersection(set(s2))
    # if there is common char return yes, otherwise no
    return 'YES' if is_common else 'NO'
