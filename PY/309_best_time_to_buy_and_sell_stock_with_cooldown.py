# 309. Best Time to Buy and Sell Stock with Cooldown Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 39075
# Total Submissions: 97207
# Difficulty: Medium
# Contributor: LeetCode
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# 
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
# 
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]

# 2017.05.14
# 3 states. s0, s1, s2
# s0[i] = max(s0[i - 1], s2[i - 1]); // Stay at s0, or rest from s2
# s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]); // Stay at s1, or buy from s0
# s2[i] = s1[i - 1] + prices[i]; // Only one way from s1
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        s0 = [ 0 for x in xrange(n)]
        s1 = [ 0 for x in xrange(n)]
        s2 = [ 0 for x in xrange(n)]
        s0[0], s1[0], s2[0] = 0, -prices[0], float('-inf')
        for i in xrange(1, n):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s2[n-1], s0[n-1])
