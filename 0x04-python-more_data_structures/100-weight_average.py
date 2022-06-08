#!/usr/bin/python3
def weight_average(my_list=[]):
    """A function that returns the weighted average of all integers tuple (<score>, <weight>) in the list
        Returns 0 if the list is empty
     """
    if len(my_list) == 0:
        return 0
    sum_score = 0
    sum_weight = 0
    for i in my_list:
        sum_score += i[0] * i[1]
        sum_weight += i[1]
    return sum_score / sum_weight
