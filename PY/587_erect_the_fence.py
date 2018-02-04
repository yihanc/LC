# 587. Erect the Fence
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
# 
# Example 1:
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
# 
# Example 2:
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
# 
# Even you only have trees in a line, you need to use rope to enclose them. 
# Note:
# 
# All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# 2018.02.04 

# This Solution implement Gift Wrapping Convex Hull algorithm. 
# https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
# complexity is O(nh), where h is the number of output. It is output sensitive algorithm

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if not points or len(points) <= 3: return points
        
        #1 Get start point, most left top point
        pstart = points[0]
        for p in points[1:]:
            if p.x < pstart.x or (p.x == pstart.x and p.y > pstart.y):
                pstart = p
        res = [pstart]
        
        #2 Start searching
        cur, nex = pstart, None
        while True:
            collinear = []                          # To save collinear points
            for p in points:
                if p == cur: continue               # Skip self
                if not nex: 
                    nex = p
                    continue
                
                cr = self.getCrossProduct(cur, nex, p)
                if cr > 0:   # cur -> p line is to the left of cur -> nex line
                    nex, collinear = p, []          # Empty collinear points if a new point
                elif cr == 0:                       # Find collinear point
                    if self.isFarther(cur, nex, p):
                        collinear, nex = collinear + [nex], p
                    else:
                        collinear += [p]

            if nex in res: break
                
            cur, nex, res = nex, None, res + collinear + [nex]
        return res + collinear


    def isFarther(self, a, b, c):   # if distance of ac is bigger than distance of ab
        sq_ab = (a.y - b.y)**2 + (a.x - b.x)**2
        sq_ac = (a.y - c.y)**2 + (a.x - c.x)**2
        return sq_ac > sq_ab
    
    
    def getCrossProduct(self, a, b, c):   # Cross product of ab and ac, if > 0, c is to the left of ab
        x1 = a.x - b.x
        y1 = a.y - b.y
        x2 = a.x - c.x
        y2 = a.y - c.y
        return y2*x1 - y1*x2
        
