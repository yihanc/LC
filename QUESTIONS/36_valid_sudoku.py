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
