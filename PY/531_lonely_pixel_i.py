# 531. Lonely Pixel I Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 4306 Total Submissions: 8229 Difficulty: Medium
# Contributors: fallcreek
# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
# 
# The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.
# 
# A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.
# 
# Example:
# Input: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
# 
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.

# 2017.05.28
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]: return 0
        m, n = len(picture), len(picture[0])
        
        rows = [ 0 for x in xrange(m) ]
        cols = [ 0 for y in xrange(n) ]
        
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] =='B':
                    rows[i] += 1
                    cols[j] += 1
        
        count = 0
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count
                     
                    
