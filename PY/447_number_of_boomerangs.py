# 447. Number of Boomerangs Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 19868
# Total Submissions: 45026
# Difficulty: Easy
# Contributors:
# alexander54
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


# 2017.05.24
# Scan and add result of each point
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0    
        n = len(points)
        for i in xrange(n):
            dic = {}
            for j in xrange(n):
                if i == j: continue
                d = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                dic[d] = dic.get(d, 0) + 1
            for k, v in dic.iteritems():
                res += v * (v - 1)
            
        return res

