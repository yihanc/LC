# 391. Perfect Rectangle Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 8944
# Total Submissions: 34853
# Difficulty: Hard
# Contributor: LeetCode
# Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
# 
# Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
# 
# 
# Example 1:
# 
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
# 
# Return true. All 5 rectangles together form an exact cover of a rectangular region.
# 
# Example 2:
# 
# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap between the two rectangular regions.
# 
# Example 3:
# 
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
# 
# Return false. Because there is a gap in the top center.
# 
# Example 4:
# 
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
# 
# Return false. Because two of the rectangles overlap with each other.


# 2017.05.28
# Algorithms
# 1. size == all small size
# 2. Points count for each corner shold be even.
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def getsize(rectangle):
            return (rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1])

        size = 0
        x1, y1 = float('inf'), float('inf')
        x2, y2 = float('-inf'), float('-inf')
        se = set()
        
        for rec in rectangles:
            x1 = min(x1, rec[0])
            y1 = min(y1, rec[1])
            x2 = max(x2, rec[2])
            y2 = max(y2, rec[3])
            size += getsize(rec)
            
            corners = [str(rec[0])+" "+str(rec[1]), str(rec[0])+" "+str(rec[3]), str(rec[2])+" "+str(rec[1]), str(rec[2])+" "+str(rec[3]) ]
            for corner in corners:
                if corner not in se:
                    se.add(corner)
                else:
                    se.remove(corner)

        if str(x1)+" "+str(y1) in se and str(x1)+" "+str(y2) in se and str(x2)+" "+str(y1) in se and str(x2)+" "+str(y2) in se and len(se) == 4:
            return getsize([x1, y1, x2, y2]) == size
        else:
            return False
        
        
            


# cases
# [[0, 0, 4, 1], [7, 0, 8, 2], [6, 2, 8, 3], [5, 1, 6, 3], [4, 0, 5, 1], [6, 0, 7, 2], [4, 2, 5, 3], [2, 1, 4, 3], [0, 1, 2, 2], [0, 2, 2, 3], [4, 1, 5, 2], [5, 0, 6, 1]]
# True

# [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
# False

