# 123. Best Time to Buy and Sell Stock III My Submissions QuestionEditorial Solution
# Total Accepted: 57441 Total Submissions: 217207 Difficulty: Hard
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# Have you met this question in a real interview? Yes  No
# Discuss
# Notes:
# Traverse once and save the maximum profit for time i
# Traverse again to find out the maximum profit i before and i after
# DP solution more concise and easier
# http://postimg.org/image/b0auzohv3/

# 2017.03.24 Rewrite. From index 1
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        res = 0
        buy1, sell1, buy2, sell2 = prices[0], 0, prices[0], 0
        
        for i in xrange(1, len(prices)):
            sell2 = max(sell2, prices[i] - buy2)
            buy2 = min(buy2, prices[i] - sell1)
            sell1 = max(sell1, prices[i] - buy1)
            buy1 = min(buy1, prices[i])
        
        return sell2
            

# 1.1.2017 DP no sys.maxint
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0

        buy1, sell1, buy2, sell2 = None, 0, None, 0
        for i in xrange(len(prices)):
            sell2 = max(sell2, buy2 + prices[i])  if buy2 != None else sell2
            buy2 = max(buy2, sell1 - prices[i]) if buy2 != None else sell1 - prices[i]
            sell1 = max(sell1, buy1 + prices[i])  if buy1 != None else sell1
            buy1 = max(buy1, - prices[i]) if buy1 != None else - prices[i]

        return sell2

# 12.03.2016 Rewrite DP
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy1, sell1, buy2, sell2 = sys.maxint, 0, sys.maxint, 0
        
        for price in prices:
            sell2 = max(sell2, price - buy2)
            buy2 = min(buy2, price - sell1)
            sell1 = max(sell1, price - buy1)
            buy1 = min(buy1, price)

        return sell2
        

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = [0] * 4
        res[0], res[2] = sys.maxint, sys.maxint
        i = 0
        print(prices)
        while i < len(prices):
            res[3] = max(res[3], prices[i] - res[2]) # 2 sell
            res[2] = min(res[2], prices[i] - res[1]) # 2 buy
            res[1] = max(res[1], prices[i] - res[0]) # 1 sell
            res[0] = min(res[0], prices[i]) # 1 buy
            print(res)
            i += 1
        return max(res[1], res[3])

if __name__ == "__main__":
    sol = Solution()
    sol.maxProfit([1, 2, 4, 3, 5, 7, 2, 4, 9, 0, 12])
    
