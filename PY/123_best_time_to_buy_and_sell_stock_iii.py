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
    
