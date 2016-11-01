# 51. N-Queens   QuestionEditorial Solution  My Submissions
# Total Accepted: 65762
# Total Submissions: 232455
# Difficulty: Hard
# Contributors: Admin
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
# 
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
# 
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        lRes = []
        self.dfs(lRes, [], 0, n)
        return lRes
    
    def dfs(self, lRes, res, dep, n):
        if dep == n:
            lRes.append(res)
            return
        
        for i in xrange(n):
            if self.isValid(res, dep, i):
                line = "." * i + "Q" + "."*(n-i-1)  #Generating line
                self.dfs(lRes, res + [line], dep+1, n)  #Note res + [line] for new object)
    
    def isValid(self, res, dep, col):
        if not res:
            return True
        n = len(res[0])
        for i in xrange(dep):
            if res[i][col] == "Q":  # Same col
                return False
            if col + dep - i < n and res[i][col+dep-i] == "Q":  # 45 Degree right
                return False
            if col - dep + i >= 0 and res[i][col-dep+i] == "Q": # 45 Degree left
                return False
        return True

        

if __name__  == "__main__":
    for i in xrange(1,11):
        res = Solution().solveNQueens(i)
        print(str(i) + ":  " + str(len(res)))
#        for matrix in res:
#            print("-----")
#            for row in matrix:
#                print(row)
