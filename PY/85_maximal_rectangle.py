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
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res, m, n = 0, len(matrix), len(matrix[0])
        
        # Initialize first height
        H = list(matrix[0])     # Convert string to list of int
        for j in xrange(n):
            H[j] = int(H[j])
        
        for i in xrange(m):
            #initiate L, R
            L = [0 for x in xrange(n)]
            R = [0 for x in xrange(n)]
            
            # Get the height and left
            for j in xrange(n):
                if i == 0:
                    pass
                elif matrix[i][j] == "1":
                    H[j] += 1
                else:
                    H[j] = 0
                
                # Get the left
                k = j - 1
                while k >= 0 and H[k] >= H[j]:
                    L[j] = L[j] + L[k] + 1
                    k = k - L[k] - 1
            
            # Get the right
            for j in reversed(xrange(n)):
                k = j + 1
                while k < n and H[j] <= H[k]:
                    R[j] = R[j] + R[k] + 1
                    k = k + R[k] + 1
            
            # Calculate area for each and update res if bigger
            for j in xrange(n):
                if H[j] != 0:
                    res = max(res, H[j] * (L[j] + R[j] + 1))
            
        return res

if __name__ == "__main__":
    A = ["10100","10111","11111","10010"]
    Solution().maximalRectangle(A)

