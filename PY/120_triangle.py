# 120. Triangle  QuestionEditorial Solution  My Submissions
# Total Accepted: 82319
# Total Submissions: 260079
# Difficulty: Medium
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
# 
# Subscribe to see which companies asked this question

# 12.03.2016
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0: return 0
        
        dp = [ 0 for j in xrange(n) ]
        dp[0] = triangle[0][0]
        
        
        i = 1
        while i < n:
            for j in xrange(i, -1, -1):
                if j == i:
                    dp[j] = dp[j-1] + triangle[i][j]
                elif j == 0:
                    dp[j] += triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            i += 1
        
        res = dp[0]
        for i in xrange(1, n):
            res = min(dp[i], res)
        
        return res

import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
            
        row, col = len(triangle), len(triangle[-1])
        A = [0] * col
        A[0] = triangle[0][0]
        res = A[0]

        for i in xrange(1, row):
            res = sys.maxint
            for j in reversed(xrange(0, i+1)):
                if j == i:
                    A[j] = A[j-1] + triangle[i][j]
                elif j != 0:
                    A[j] = min(A[j], A[j-1]) + triangle[i][j]
                else:
                    A[j] += triangle[i][j]
                    
                res = min(res, A[j])
        
        return res
                
                
if __name__ == "__main__":
    A = [
        [-1], [2,3], [1,-1,-1]
        ]

    Solution().minimumTotal(A)
        
