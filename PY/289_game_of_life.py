# 289. Game of Life Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 44368
# Total Submissions: 121291
# Difficulty: Medium
# Contributor: LeetCode
# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# 
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# 
# Follow up: 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


# 2017.05.14 Scan and check
# o( 8 * m, n)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        pairs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        flipmap = []
        for i in xrange(m):
            for j in xrange(n):
                live_neighbors = 0
                for pair in pairs:
                    ii, jj = i + pair[0], j + pair[1]
                    if ii < m and ii >= 0 and jj < n and jj >= 0 and board[ii][jj] == 1:
                        live_neighbors += 1
                if ( (board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3))
                    or (board[i][j] == 0 and live_neighbors == 3)):
                    flipmap.append([i,j])
        for i, j in flipmap:
            board[i][j] = 0 if board[i][j] == 1 else 1

