# 533. Lonely Pixel II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 2363 Total Submissions: 5879 Difficulty: Medium
# Contributors: fallcreek
# Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:
# 
# Row R and column C both contain exactly N black pixels.
# For all rows that have a black pixel at column C, they should be exactly the same as row R
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
# 
# Example:
# Input:                                            
# [['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'B', 'W', 'B', 'B', 'W'],    
#  ['W', 'W', 'B', 'W', 'B', 'W']] 
# 
# N = 3
# Output: 6
# Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
#         0    1    2    3    4    5         column index                                            
# 0    [['W', 'B', 'W', 'B', 'B', 'W'],    
# 1     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 2     ['W', 'B', 'W', 'B', 'B', 'W'],    
# 3     ['W', 'W', 'B', 'W', 'B', 'W']]    
# row index
# 
# Take 'B' at row R = 0 and column C = 1 as an example:
# Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
# Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.
# 
# Note:
# The range of width and height of the input 2D array is [1,200].

# 2017.05.28
# rows + cols. 
class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        if not picture or not len(picture[0]): return 0
        m, n = len(picture), len(picture[0])
        rows = [ 0 for _ in xrange(m) ]
        cols = [ 0 for _ in xrange(n) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for j in xrange(n):
            totest = []
            for i in xrange(m):
                if rows[i] != N or rows[i] != cols[j] : continue
                
                if picture[i][j] == 'B': 
                    totest.append(i)
                    
            if len(totest) != N: continue
            allsame = True if len(totest) > 0 else False
            for row in xrange(1, len(totest)):
                if picture[totest[row]] != picture[totest[row-1]]:
                    allsame = False
                    break
            if allsame: count += len(totest)

        return count

# cases
# ["WBWBBW","WBWBBW","WBWBBW","BWBWWB"]
# 2
# Expected: 0


# ["WBWBBW","BWBWWB","WBWBBW","BWBWWB","WBWBBW","BWBWWB"]
# 3
# expected: 0
