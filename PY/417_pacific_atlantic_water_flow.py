# 417. Pacific Atlantic Water Flow Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 12816
# Total Submissions: 38574
# Difficulty: Medium
# Contributor: LeetCode
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
# 
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
# 
# Given the following 5x5 matrix:
# 
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


# 2017.05.27
# Too slow
# Two queues for Pacific cells and Atlantic cells each
# Save result in set of each. 
# Find intercetion of two sets
from collections import deque
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])

        pq, aq = deque(), deque()   #pq, pacific queue, aq atlantic quee
        for j in xrange(n): 
            pq.appendleft([0, j])
            aq.appendleft([m - 1, j])
        for i in xrange(m):         # Added (0, 0) and (m-1, n-1) twice but it is fine
            pq.appendleft([i, 0])
            aq.appendleft([i, n - 1])
        paci_set = self.getSet(matrix, pq, m, n)
        atla_set = self.getSet(matrix, aq, m, n)

        res = []
        for x in paci_set.intersection(atla_set):
            res.append([x / n, x % n])
        return res
    
    def getSet(self, matrix, d, m, n):  # BFS search all cells and save in a set
        res = set()
        pairs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while d:
            i, j = d.pop()
            res.add(i * n + j)
            for pair in pairs:
                ii, jj = i + pair[0], j + pair[1]
                if ii < m and ii >= 0 and jj < n and jj >= 0 and ii * n + jj not in res and matrix[ii][jj] >= matrix[i][j]:
                    d.appendleft([ii, jj])

        return res
