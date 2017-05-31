# 54. Spiral Matrix   QuestionEditorial Solution  My Submissions
# Total Accepted: 77608
# Total Submissions: 322146
# Difficulty: Medium
# Contributors: Admin
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
# 
# Subscribe to see which companies asked this question

# 2017.05.28 Rewrite
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        
        lvl = 0
        res = []
        while lvl < (min(m, n)+1) / 2:
            for j in xrange(lvl, n - lvl):
                res.append(matrix[lvl][j])
            
            for i in xrange(lvl + 1, m - lvl):
                res.append(matrix[i][n-1-lvl])
            
            if m - 1 - lvl == lvl or n - 1 - lvl == lvl: break
        
            for j in xrange(n - 2 - lvl, lvl - 1, -1):
                res.append(matrix[m-1-lvl][j])
            
            for i in xrange(m - 2 - lvl, lvl, -1):
                res.append(matrix[i][lvl])
            
            lvl += 1
        return res
        
            
        

# 12.18.2016 Rewrite
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        
        lvl = 0
        while lvl < (min(m, n) + 1) // 2:
            for j in xrange(lvl, n - lvl):
                res.append(matrix[lvl][j])
            
            for i in xrange(lvl + 1, m - lvl):
                res.append(matrix[i][n - lvl - 1])
            
            if lvl == m - lvl - 1 or lvl == n - lvl - 1:
                break
                
            for j in xrange(n - lvl - 2, lvl - 1, -1):
                res.append(matrix[m - lvl - 1][j])
        
            for i in xrange(m - lvl - 2, lvl, -1):
                res.append(matrix[i][lvl])
            
            lvl += 1
        
        return res
            

# 11.26.2016 Rewrite. One pass
# Use lvl = 0, Top -> Right -> Bot -> left
# If m - lvl - 1 == lvl or n - lvl -1 == lvl, break after Top -> Right -> Break
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        
        res = []
        
        lvl = 0
        while lvl < (min(m, n) + 1 ) // 2:
            for j in xrange(lvl, n-lvl):       #Top row
                res.append(matrix[lvl][j])
            
            for i in xrange(lvl+1, m-lvl):      #Right col
                res.append(matrix[i][n-lvl-1])
            
            if (m - lvl - 1) == lvl or (n - lvl - 1) == lvl:    # Only one row or one col left
                break
            
            j = n - lvl - 2
            while j >= lvl:
                res.append(matrix[m-lvl-1][j])
                j -= 1
            
            i = m - lvl - 2
            while i > lvl:
                res.append(matrix[i][lvl])
                i -= 1
                    
            lvl += 1
        
        return res


class Solution2(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        
        lvl = 0
        while lvl < (min(m,n)+1)//2:    #1,2 = 1, 3,4 = 2 , 5,6 = 3
            i, j = lvl, lvl
            while j < n - lvl:  # Top row
                print("a" + str(i) + str(j))
                res.append(matrix[i][j])
                j += 1
            
            i, j = i+1, j-1             # Reset to the corret pos
            print("HERE" + str(i) + str(j))

            while i < m - lvl: # Right row
                print("b" + str(i) + str(j))
                res.append(matrix[i][j])
                i += 1

            i, j = i-1, j-1
            while i != lvl and j >= lvl: # Bot row
                print("c" + str(i) + str(j))
                res.append(matrix[i][j])
                j -= 1
            
            i, j = i-1, j+1
            while i >= lvl + 1 and j != n - lvl - 1: # Left row, j != n - lvl - 1 to avoid the same col
                print("d" + str(i) + str(j))
                res.append(matrix[i][j])
                i -= 1
                
            lvl += 1
        
        return res

if __name__  == "__main__":
    #matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    #matrix = [[1,2,3], [4,5,6], [7,8,9]]
    #matrix = [[2,3,4,5,6]]
    matrix = [[7], [9], [6]]
    for row in matrix:
        print(row)
    print(Solution().spiralOrder(matrix))
