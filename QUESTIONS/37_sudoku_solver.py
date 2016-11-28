# 37. Sudoku Solver My Submissions QuestionEditorial Solution
# Total Accepted: 51072 Total Submissions: 201773 Difficulty: Hard
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# 
# You may assume that there will be only one unique solution.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    found = False
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for x in xrange(81):
            if board[x//9][x%9] == '.':
                break

        self.dfs(board, x//9, x%9)
        return
    
    def dfs(self, board, i, j):
        for row in board:
            print(row)
        if i == 9 and j == 0:
            self.found = True
            return
        
        if self.found: return
    
        nums = self.getCandidates(board, i, j)
        print(i, j, nums)
        
        x = i * 9 + j + 1
        while x < 81:
            if board[x//9][x%9] == '.':
                break
            x += 1
        
        for num in nums:
            board[i] = board[i][:j] + num + board[i][j+1:]
            self.dfs(board, x // 9, x % 9)
            if self.found: return
            board[i] = board[i][:j] + '.' + board[i][j+1:]
            
    def getCandidates(self, board, i, j):
        n = 9
        nums = [ str(x) for x in xrange(1, n+1) ]
        for x in xrange(n):
            c1, c2, c3 = board[i][x], board[x][j], board[i // 3 * 3 + x // 3][j // 3 * 3 + x % 3]
            if c1 != '.' and c1 in nums:
                nums.remove(c1)
            if c2 != '.' and c2 in nums:
                nums.remove(c2)
            if c3 != '.' and c3 in nums:
                nums.remove(c3)
        return nums
    

if __name__ == "__main__":
    A = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    for row in A:
        print(row)
    Solution().solveSudoku(A)
