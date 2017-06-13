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


# 2017.05.31
# Another clearer version
# However, hq.remove is too slow. It will get TLE for large case
from heapq import *
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        height = []
        for a,b,c in buildings:
            height.append([a, -c])  # LEFT HEIGHT to negative so that it appears first than right HEIGHT
            height.append([b, c])
            
        s_height = sorted(height, key = lambda x: [x[0], x[1]]) # Sort by left side, rigth side
        
        hq = [0]
        prev = 0
        for h in s_height:
            if h[1] < 0:        # A left side
                heappush(hq, h[1])
            else:               # Right side
                hq.remove(-h[1])
                heapify(hq)
            cur = -hq[0]
            if prev != cur:
                res.append([h[0], cur])
                prev = cur
            
        return res


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        n = len(buildings)
        
        # Pre-process to remove covered and get max right
        i = 1
        rmax = buildings[0][1]
        while i < n:
            l1, r1, h1 = buildings[i - 1]
            l2, r2, h2 = buildings[i]
            
            if r2 <= r1 and h2 <= h1:
                del buildings[i]
                n -= 1
                continue
            
            rmax = max(rmax, r2)
            i += 1
        
        nums = [ 0 for x in xrange(rmax + 1) ]
#        print(buildings)
        n = len(buildings)
        
        for i in xrange(n):
            l1, r1, h1 = buildings[i]
            print(l1, r1, h1)

#            nums[l1] = max(nums[l1], h1)
#            nums[r1] = max(nums[r1], h1)
            for x in xrange(l1, r1):
                nums[x] = max(nums[x], h1)
            print(nums)
#                if nums[x+1] < nums[x]:
#                    nums[x] = min(nums[x], h2)
        print(nums)
        res = []
        for i in xrange(len(nums)):
            if (i == 0 and nums[i] != 0 ) or nums[i] != nums[i-1]:
                res.append([i, nums[i]])
        
        return res
                            
                
# Online answer. 2017.03.05
from heapq import *

class Solution(object):
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:  # L < Last R? (Overlap)
                x = LRH[i][0]       # x = cur L
                while i < n and LRH[i][0] == x:             # While L are equal, keep pushing.
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:   #   if No overlap with the highest Rec. Clean up HQ.
                x = -liveHR[0][1]       # Get the R of the current highest H
                while liveHR and -liveHR[0][1] <= x:        # Pop all points that to the left.
                    heappop(liveHR)
            height = -liveHR[0][0] if len(liveHR) > 0 else 0
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
        

# Test cases
# 1. [ [2, 9, 10], [3, 7 ,15], [5 ,12 ,12], [15, 20 ,10], [19, 24 ,8] ]
# Expected: [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]
# 2. [[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]
#
# 3. [[0,1,3]]
# Expected [[0,3],[1,0]]
#
# 4. [[0,2147483647,2147483647]]
# 
# 5. [[1,2,1],[2147483646,2147483647,2147483647]] MLE
#

if __name__ == "__main__":
#    A = [ [2, 9, 10], [3, 7 ,15], [5 ,12 ,12], [15, 20 ,10], [19, 24 ,8] ]
    A = [[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]
#    A = [[0,2147483647,2147483647]]
    print(A)
    print(Solution().getSkyline(A))

