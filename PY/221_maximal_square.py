# 221. Maximal Square Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 54501
# Total Submissions: 196411
# Difficulty: Medium
# Contributors: Admin
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 

# 2017.03.18 Same deque method as max rectangle
from collections import deque
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        heights = [ 0 for x in xrange(n + 1) ]
        
        for i in xrange(m):
            for j in xrange(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
            
            print(heights)
            res = max(res, self.maxArea(heights))
        return res
    
    def maxArea(self, heights):
        d = deque()
        res = 0
        
        for i in xrange(len(heights)):
            while d and heights[d[-1]] >= heights[i]:
                h = heights[d.pop()]
                side = d[-1] if d else -1
                res = max(res, min(h, i - side - 1) ** 2)
            d.append(i)
        return res
                
        
        

