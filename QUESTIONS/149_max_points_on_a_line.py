# 149. Max Points on a Line   QuestionEditorial Solution  My Submissions
# Total Accepted: 69049
# Total Submissions: 450757
# Difficulty: Hard
# Contributors: Admin
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# 
# Subscribe to see which companies asked this question
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n == 1:      # Corner case.
            return 1
        dic = {}
        res = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
#                print(points[i].x, points[i].y, points[j].x, points[j].y)
                if points[j].x == points[i].x and points[j].y == points[i].y:   # Same position
                    key = str(points[i].x) + "S" + str(points[i].y)
                elif points[i].x == points[j].x:            # Vertical line
                    key = "V" + str(points[i].x)
                elif points[i].y == points[j].y:            # Horizontal line 
                    key = "H" + str(points[i].y)
                else:
                    s = (float(points[j].y - points[i].y ) / (points[j].x - points[i].x))
                    b = points[i].y - s * points[i].x       # Y = sX + b, B = Y - sX
                    key = str(round(s,3)) + "X" + str(round(b,3))   #Other cases

                if key not in dic:
                    dic[key] = set()
                    
                dic[key].add(i)
                dic[key].add(j)
                res = max(res, len(dic[key]))

        print(dic)
        return res
        

if __name__ == "__main__":
    #A = [[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
    #A = [[0,0],[1,1],[1,-1]]
    A = [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]
    points = []
    for i, j in A:
        cur = Point(i, j)
        points.append(cur)

#    for point in points:
#        print(point.x, point.y)
        
    print(Solution().maxPoints(points))
