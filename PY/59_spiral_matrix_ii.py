# 59. Spiral Matrix II   QuestionEditorial Solution  My Submissions
# Total Accepted: 66407
# Total Submissions: 177849
# Difficulty: Medium
# Contributors: Admin
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# 
# For example,
# Given n = 3,
# 
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
# Subscribe to see which companies asked this question

# Same template as spiral matrix 
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [ [0 for x in xrange(n)] for y in xrange(n)]
        
        lvl, num = 0, 1
        while lvl < (n + 1 // 2):
            i, j = lvl, lvl
            while j < n - lvl:
                res[i][j] = num
                num += 1
                j += 1
            
            i, j = i+1, j-1
            while i < n - lvl:
                res[i][j] = num
                num += 1
                i += 1
        
            i, j = i-1, j-1
            while i != lvl and j >= lvl:
                res[i][j] = num
                num += 1
                j -= 1
            
            i, j = i-1, j+1
            while i >= lvl + 1 and j != n - lvl - 1:
                res[i][j] = num
                num += 1
                i -= 1
            
            lvl += 1
        
        return res
            

if __name__  == "__main__":
    for n in xrange(5):
        print("-----" + str(n) + "-----")
        res = Solution().generateMatrix(n)
        for row in res:
            print(row)
