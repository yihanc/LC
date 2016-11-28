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

# 11.22.2016 Rewrite
# Idea:
# DFS. Calculate Candidates of current cell. Find next cell. 
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
        if i == 9 and j == 0:
            self.found = True
            return
        
        if self.found: return
    
        nums = self.getCandidates(board, i, j)
        
        x = i * 9 + j + 1
        while x < 81:
            if board[x//9][x%9] == '.':
                break
            x += 1
        
        for num in nums:
            board[i][j] = num
            self.dfs(board, x // 9, x % 9)
            if self.found: return
            board[i][j] = '.'
            
    
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
        
            

class Solution2(object):
    ansFound = False
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0, 0)
        return
    
    def dfs(self, board, lastI, lastJ):
        if self.ansFound:
            return
        
        i, j = self.getNext(board, lastI, lastJ)
        
        if i == -1 and j == -1:
            self.ansFound = True
            return

#        print(str(i) + " " + str(j))
        nums = self.getCandidates(board, i, j)
#        print("getCandidates : ", nums)
        for num in nums:
            #board[i] = board[i][:j] + num + board[i][j+1:]     #If board is string
            board[i][j] = num
            self.dfs(board, i, j)
            if self.ansFound:
                return
            board[i][j] = '.'
            #board[i] = board[i][:j] + '.' + board[i][j+1:]  
                    
    def getNext(self, board, lastI, lastJ):
        start = lastI * 9 + lastJ       #Find i,j to process
        for x in xrange(start, 81):
            i, j = x // 9, x % 9
            if board[i][j] == '.':
                return [i, j]
        return [-1, -1]
    
    def getCandidates(self, board, i, j):
        candidates = [ str(x) for x in xrange(1, 10) ]
        
        for col in xrange(9):
            if board[i][col] in candidates:
                candidates.remove(board[i][col])
        
        for row in xrange(9):
            if board[row][j] in candidates:
                candidates.remove( board[row][j])
        
        lt_i, lt_j = i // 3 * 3, j // 3 * 3
        for row in xrange(lt_i, lt_i + 3):
            for col in xrange(lt_j, lt_j + 3):
                if board[row][col] in candidates:
                    candidates.remove(board[row][col])
        
        return candidates
    
    

if __name__ == "__main__":
    #board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    board = [list("53..7...."),
            list("6..195..."),
            list(".98....6."),
            list("8...6...3"),
            list("4..8.3..1"),
            list("7...2...6"),
            list(".6....28."),
            list("...419..5"),
            list("....8..79")]
    print("----------")
        

    Solution().solveSudoku(board)
    for row in board:
        print(row)
