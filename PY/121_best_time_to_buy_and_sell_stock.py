# 121. Best Time to Buy and Sell Stock My Submissions QuestionEditorial Solution
# Total Accepted: 102364 Total Submissions: 282834 Difficulty: Easy
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No

# 2018.03.10

# 2017.03.23 Stock questions Rewrite
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        res = 0
        buy = prices[0]
        profit = 0
        
        for i in xrange(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])

        return profit

# 12.3.2016
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        res, buy = 0, prices[0]
        
        for price in prices:
            buy = min(buy, price)
            res = max(res, price - buy)
        
        return res

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0

        buy, mx = 0, 0
        i = 1
        while i < len(prices):
            if prices[i] > prices[i-1]:
                mx = max(mx, prices[i] - prices[buy])
            if prices[i] < prices[buy]:
                buy = i
            i += 1
        return mx

# DP algorithm inspired by stock iii
#
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         res = [0] * 2
#         res[0] = -sys.maxint
#         
#         i = 0
#         while i < len(prices):
#             res[1] = max(res[1], prices[i] - res[0])
#             res[0] = min(res[0], prices[i])
#             i += 1
#         return res[1]
# 
