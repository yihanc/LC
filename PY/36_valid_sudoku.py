# 36. Valid Sudoku My Submissions QuestionEditorial Solution
# Total Accepted: 76248 Total Submissions: 245587 Difficulty: Easy
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# 
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# 
# 
# A partially filled sudoku which is valid.
# 
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

# 12.17 2016, 3 dics
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        for i in xrange(m):
            mp1 = { x : False for x in "123456789" }
            mp2 = { x : False for x in "123456789" }
            mp3 = { x : False for x in "123456789" }
            
            for j in xrange(n):
                c1, c2, c3 = board[i][j], board[j][i], board[i//3*3+j//3][i%3*3 + j%3]
                if c1 != "." and mp1[c1]: return False
                if c2 != "." and mp2[c2]: return False
                if c3 != "." and mp3[c3]: return False
                
                if c1 != ".": mp1[c1] = True
                if c2 != ".": mp2[c2] = True
                if c3 != ".": mp3[c3] = True
                    
        return True

# 11.22.2016 Rewrite. 3 loop 1 dic
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        dic = {}
        
        for i in xrange(n):
            for j in xrange(n):
                if board[i][j] in dic:
                    return False
                if board[i][j] != '.':
                    dic[board[i][j]] = 1
            dic = {}
        
        for j in xrange(n):
            for i in xrange(n):
                if board[i][j] in dic:
                    return False
                if board[i][j] != '.':
                    dic[board[i][j]] = 1
            dic = {}
        
        for i in xrange(n):
            for j in xrange(n):
                row, col = i // 3 * 3 + j // 3, i % 3 * 3 + j % 3
                if board[row][col] in dic:
                    return False
                if board[row][col] != '.':
                    dic[board[row][col]] = 1
            dic = {}
        return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        print(board)
        
        # row
        for i in xrange(9):
            dic = {}
            for j in xrange(9):
                if board[i][j] == ".": 
                    continue
                else:
                    if board[i][j] in dic: 
                        return False
                    else: 
                        dic[board[i][j]] = True
            print(dic)
        
        # col
        for i in xrange(9):
            dic = {}
            for j in xrange(9):
                if board[j][i] == ".": 
                    continue
                else:
                    if board[j][i] in dic:
                        return False
                    else:
                        dic[board[j][i]] = True
            print(dic)

        # zone
        for k in [0,3,6]:
            for l in [0,3,6]:               #Left corner of each zone
                dic = {}
                for i in xrange(3):
                    for j in xrange(3):
                        print(board[k+i][l+j])
                        if board[k+i][l+j] == ".": 
                            continue
                        else:
                            if board[k+i][l+j] in dic:
                                return False
                            else:
                                dic[board[k+i][l+j]] = True
                print(dic)
                        
        return True

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        A = Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
        self.assertEqual(A, True)

    def test_1(self):
        A = Solution().isValidSudoku(["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."])
        self.assertEqual(A, True)

if __name__ == "__main__":
    unittest.main()
