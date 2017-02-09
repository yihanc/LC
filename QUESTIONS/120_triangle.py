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

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle: return 0
        n = len(triangle)
        
        dp = [ 0 for i in xrange(n) ]
        res = None
        
        for i in xrange(n):
            for j in xrange(i, -1, -1):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j != 0 and j == i :
                    dp[j] = dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
                
                if i == n - 1:
                    res = min(res, dp[j]) if res != None else dp[j]
#                    if res is None:
#                        res = dp[j]
#                    else:
#                        res = min(res, dp[j])
            print(dp)
                    
        return res
            
        
                
if __name__ == "__main__":
    A = [
        [-1], [2,3], [1,-1,-1]
        ]

    print(Solution().minimumTotal(A))
        
