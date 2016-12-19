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

# 12.18.2016 Rewrite
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        if n == 1: return [[1]]
        
        res = [ [ 0 for j in xrange(n) ] for i in xrange(n) ]
        
        lvl, count = 0, 1
        while lvl < (n + 1) // 2:
            for j in xrange(lvl, n - lvl):
                res[lvl][j], count = count, count + 1
            
            for i in xrange(lvl + 1, n - lvl):
                res[i][n - lvl - 1], count = count, count + 1
            
            if lvl == n - lvl - 1: break
                
            for j in xrange(n - lvl - 2, lvl - 1, -1):
                res[n - lvl - 1][j], count = count, count + 1
            
            for i in xrange(n - lvl - 2, lvl, -1):
                res[i][lvl], count = count, count + 1
            
            lvl += 1
        
        return res


# 11.26.2016 Rewrite
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        res = [[ 0 for j in xrange(n)] for i in xrange(n)]
        
        lvl = 0
        num = 1
        while lvl < (n + 1) // 2:
            for j in xrange(lvl, n - lvl):
                res[lvl][j] = num
                num += 1
            
            for i in xrange(lvl + 1, n - lvl):
                res[i][n-lvl-1] = num
                num += 1
            
            if n - lvl - 1 == lvl or n - lvl - 1 == lvl:
                break
            
            for j in xrange(n-lvl-2, lvl-1, -1):
                res[n-lvl-1][j] = num
                num += 1
            
            for i in xrange(n-lvl-2, lvl, -1):
                res[i][lvl] = num
                num += 1
            
            lvl += 1
            
        return res

# Same template as spiral matrix 
class Solution2(object):
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
