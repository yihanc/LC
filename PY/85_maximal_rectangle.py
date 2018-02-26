# 85. Maximal Rectangle  QuestionEditorial Solution  My Submissions
# Total Accepted: 50686
# Total Submissions: 202962
# Difficulty: Hard
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
# 
# For example, given the following matrix:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
# Subscribe to see which companies asked this question

# 2018.02.24 Used a list comprehension
from collections import deque
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        heights = [0] * n
        for i in xrange(m):
            heights = [ x + int(y) if y != "0" else 0 for x,y in zip(heights, matrix[i])]
            res = max(res, self.getMaxHeight(heights))
        return res
        
    
    def getMaxHeight(self, heights):
        res = 0
        heights = heights + [0]
        d = deque()
        for i in xrange(len(heights)):
            while d and heights[i] < heights[d[-1]]:
                h = heights[d.pop()]
                left = d[-1] if d else -1
                res = max(res, h * (i - left - 1))
            d.append(i)
        return res
            

# 2017.03.18 One stack solution
from collections import deque
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        heights = [ 0 for y in xrange(n + 1) ]
        
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                heights[j] = 0 if matrix[i][j] == "0" else heights[j] + int(matrix[i][j])
            
            res = max(res, self.maxArea(heights))

        return res
        
    def maxArea(self, heights):
        res = 0
        d = deque()
        
        for i in xrange(len(heights)):
            while d and heights[d[-1]] >= heights[i]:
                h = heights[d.pop()]
                side = d[-1] if d else -1
                res = max(res, h * (i - side - 1))
            d.append(i)

        return res

# 12.30.2016 rewrite
from collections import deque

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        heights = [ [ 0 for j in xrange(n + 1) ] for i in xrange(m) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and matrix[i][j] == "1":
                    heights[i][j] = 1
                elif matrix[i][j] == "1":
                    heights[i][j] += heights[i-1][j] + 1
                else:
                    pass
        
        for i in xrange(m):
            d = deque()
            for j in xrange(n + 1):
                while d and heights[i][j] < heights[i][d[-1]]:
                    index = d.pop()
                    h = heights[i][index]
                    l = -1 if not d else d[-1]
                    side = j - l - 1
                    res = max(res, h * side)
                d.append(j)
                
        return res
        

# 11.29.2016 Rewrite
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        heights = []
        res = 0
        
        for i in xrange(m):
            if i == 0:
                heights = [ int(digit) for digit in matrix[0] ] 
                heights.append(0)
            else:
                for j in xrange(n):
                    if matrix[i][j] == "1":
                        heights[j] += int(matrix[i][j])
                    else:
                        heights[j] = 0
            
            d = []
            j, l = 0, -1
            while j < len(heights):
                while d and heights[d[-1]] >= heights[j]:
                    index = d.pop()
                    h = heights[index]
                    if d:
                        l = d[-1]
                    else:
                        l = -1
                    res = max(res, h * (j - 1 - l))
                    
                d.append(j)
                j += 1
            
        return res

if __name__ == "__main__":
    A = ["10100","10111","11111","10010"]
    print(Solution().maximalRectangle(A))

# 
# 
# class Solution2(object):
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#         if not matrix:
#             return 0
#         res, m, n = 0, len(matrix), len(matrix[0])
#         
#         # Initialize first height
#         H = list(matrix[0])     # Convert string to list of int
#         for j in xrange(n):
#             H[j] = int(H[j])
#         
#         for i in xrange(m):
#             #initiate L, R
#             L = [0 for x in xrange(n)]
#             R = [0 for x in xrange(n)]
#             
#             # Get the height and left
#             for j in xrange(n):
#                 if i == 0:
#                     pass
#                 elif matrix[i][j] == "1":
#                     H[j] += 1
#                 else:
#                     H[j] = 0
#                 
#                 # Get the left
#                 k = j - 1
#                 while k >= 0 and H[k] >= H[j]:
#                     L[j] = L[j] + L[k] + 1
#                     k = k - L[k] - 1
#             
#             # Get the right
#             for j in reversed(xrange(n)):
#                 k = j + 1
#                 while k < n and H[j] <= H[k]:
#                     R[j] = R[j] + R[k] + 1
#                     k = k + R[k] + 1
#             
#             # Calculate area for each and update res if bigger
#             for j in xrange(n):
#                 if H[j] != 0:
#                     res = max(res, H[j] * (L[j] + R[j] + 1))
#             
#         return res
