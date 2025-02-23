# Question
# You are given an array called Rates, where rates[i] represents the currency price on the ith day.


# You are also given an array called Strategy, where strategy[i] represents an operation. Each operation could be -1 for buy, 0 for hold, and 1 for sell


# You are also given k, which is guaranteed to be an even integer.


# You can change the Strategy array like so:


# choose a range of k consecutive elements
# set the first half of this range to 0
# set the second half to 1
# Choose an optimal range to change the Strategy array so as to maximise the profit from executing the strategy. Return this maximum profit


# The profit is defined as the sum of all selling rates minus the sum of all buying rates. For example, if rates = [2, 3, 4, 5] and strategy = [1, 0, 0, -1], then your total profit would be (2 * 1) + (5 * -1) = -3


# rates = [2, 4, 1, 5, 10, 6]
# strategy = [-1, 1, 0, 1, -1, 0]
# k = 4
# Max profit = 18


