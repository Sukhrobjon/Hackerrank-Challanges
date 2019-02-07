import random

def sample(histogram):
    cumulative_num = 0
    sum_values = sum(histogram.values())
    ran_num = random.randint(0, sum_values - 1)
    for key, value in histogram.items():
        cumulative_num += value
        if cumulative_num > ran_num:
            return key
        else:
            continue
histogram = {'fish': 4, 'one': 1, 'two': 1, 'blue': 1, 'red': 1}