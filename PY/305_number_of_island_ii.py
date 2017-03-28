# [46] 305    Number of Islands II
# 
# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.
# 
# Example
# Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].
# 
# return [1,1,2,2].
# Note 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

class Solution(object):
    def numberIsland(self, m, n, A):
        """
        :type m: int
        :type n: int
        :type A: List[List[int]]
        :rtype: int
        """
        if m == 0 or n == 0: return 0
        res = 0
        vis = [ [ y for y in xrange(n) ] for x in xrange(m) ]
        
        


if __name__ == "__main__":
    m = 3
    n = 3
    A = [ [0,0], [0,1], [2,2], [2,1] ]
    Solution().numberIsland(m, n, A)
