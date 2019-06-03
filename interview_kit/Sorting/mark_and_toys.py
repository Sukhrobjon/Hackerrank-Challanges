"""
    Problem: https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

    Date: 06/02/2019
    Author: Sukhrobjon Golibboev
    
"""

def max_number_of_toys(prices, budget):
    """
        Takes list of unordered prices and the budget the person has
        Return an integer representing the maximum number of toys he can purchase.
    """
    # keep track of sum of the possible items
    sum = 0
    # count number of items he can afford
    count = 0
    
    sorted_price = sorted(prices)
    for item in sorted_price:
        # keep adding if he has enough budget
        if sum <= budget:
            sum += item
            count += 1
        else:
            break
    # we need to subtrack the 1 since the plus operator we are using is pre-increment
    # and will add the last item even the person can not buy that last item 
    return count - 1


prices = [1, 12, 5, 111, 200, 1000, 10]
budget = 50
print(max_number_of_toys(prices, budget))
