# 312. Burst Balloons
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 25228
# Total Submissions: 59741
# Difficulty: Hard
# Contributor: LeetCode
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
# 
# Find the maximum coins you can collect by bursting the balloons wisely.
# 
# Note: 
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 <= n <= 500, 0 <= nums[i] <= 100
# 
# Example:
# 
# Given [3, 1, 5, 8]
# 
# Return 167
# 
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.

class Solution(object):
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]
    
        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                print(left, right)
                for i in xrange(left + 1,right):
                    print(nums[left] * nums[i] * nums[right], dp[left][i] , dp[i][right])
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
            for row in dp:
                print(row)
        return dp[0][n - 1]


nums = [3,1,5,8]
Solution().maxCoins(nums)
