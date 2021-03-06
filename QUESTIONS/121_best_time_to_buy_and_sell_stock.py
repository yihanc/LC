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
