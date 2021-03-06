# 218. The Skyline Problem Add to List
# Description  Submission  Solutions
# Total Accepted: 35902
# Total Submissions: 137089
# Difficulty: Hard
# Contributors: Admin
# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
# 
#  Buildings Skyline Contour
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# The number of buildings in any input list is guaranteed to be in the range [0, 10000].
# The input list is already sorted in ascending order by the left x position Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
# Credits:
# Special thanks to @stellari for adding this problem, creating these two awesome images and all test cases.
# 
# Subscribe to see which companies asked this question.

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
                



if __name__ == "__main__":
    buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] 
    print(buildings)
    print("Expecting: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]")
    print(Solution().getSkyline(buildings))
