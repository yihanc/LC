# 130. Surrounded Regions   QuestionEditorial Solution  My Submissions # Total Accepted: 66921
# Total Submissions: 390322
# Difficulty: Medium
# Contributors: Admin
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
# 
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# 
# X X X X
# X X X X
# X X X X
# X O X X
# Subscribe to see which companies asked this question


# BFS Algorithms:
# 1. Scan bondaries and appendleft to deque()
# 2. pop, check adjancet and push to deque()
# 3. Rescan mid board and flip not in isVis

# Notes:
# 'O' not 0
# OJ input is list

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
