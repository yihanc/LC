# 122. Best Time to Buy and Sell Stock II My Submissions QuestionEditorial Solution
# Total Accepted: 87690 Total Submissions: 206180 Difficulty: Medium
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# Discuss
# Analysis:
# If current > current - 1, update mx = mx + price[cur] - price[cur - 1]
# If current < current - 1

# 12.03.2016 Rewrite
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        
        return res

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        mx = 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                mx += prices[i] - prices[i-1]
            i += 1

        return mx
        
