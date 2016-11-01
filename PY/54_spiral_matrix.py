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
class Solution(object):
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
