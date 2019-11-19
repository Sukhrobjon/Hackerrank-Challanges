# Complete the timeInWords function below.
def timeInWords(hour, minutes):
    """
    Returns the time in words
    """
    num_to_word = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "quarter", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "half",
        40: "forty", 45: "quarter", 50: "fifty"
    }

    if minutes == 0:
        return (f"{num_to_word[hour]} o' clock")
    elif 1 <= minutes <= 30:
        if minutes == 15 or minutes == 30:
            return (f"{num_to_word[minutes]} past {num_to_word[hour]}")
        if 21 <= minutes <= 29:
            last_digit = minutes - 20
            last_digit = num_to_word[last_digit]
            return (f"{num_to_word[20]} {last_digit} minutes past {num_to_word[hour]}")
        else:
            return (f"{num_to_word[minutes]} minutes past {num_to_word[hour]}")
    else:
        if minutes == 45:
            return (f"{num_to_word[60-minutes]} to {num_to_word[hour+1]}")
        if 31 <= minutes <= 39:
            remainder_20 = 60 - minutes
            last_digit = remainder_20 - 20
            last_digit = num_to_word[last_digit]
            return (f"{num_to_word[20]} {last_digit} minutes to {num_to_word[hour+1]}")
        else:
            return (f"{num_to_word[60-minutes]} minutes to {num_to_word[hour+1]}")

print(timeInWords(4, 45))
