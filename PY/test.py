
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param: n: An integer
    @param: m: An integer
    @param: operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, m, n, operators):
        # write your code here
        roots = [ x for x in xrange(n * m) ]
        vis = {}
        pairs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        cnt, res = 0, []
        for x, y in operators:
            cnt += 1
            if (x,y) in vis: continue
            vis[(x, y)] = True
            r1 = self.find(roots, x * n + y)
            for pair in pairs:
                xx, yy = x + pair[0], y + pair[1]
                if xx >= 0 and xx < m and yy >= 0 and yy < n and (xx, yy) in vis:
                    r2 = self.find(roots, xx * n + yy)
                    if r1 != r2:
                        roots[r2] = r1
                        cnt -= 1
                    print("----------------", x, y, xx, yy, r1, r2)
                    for row in xrange(m):
                        print(roots[row*n:row*n+n])
            print("cnt ", cnt, x, y)
            res.append(cnt)
        print(res)
        return res
                    

    def find(self, roots, i):
#        print("finding root", roots[i], i, roots[i] == i)
        if roots[i] != i:
            roots[i] = self.find(roots, roots[i])
        return roots[i]

# n = 4
# m = 5
# operators = [[1,1],[1,2],[1,3],[1,4]]
# n = 8
# m = 14
# operators = [[0,9],[5,4],[0,12],[6,9],[6,5],[0,4],[4,11],[0,0],[3,5],[6,7],[3,12],[0,5],[6,13],[7,5],[3,6],[4,4],[0,8],[3,1],[4,6],[6,1],[5,12],[3,8],[7,0],[2,9],[1,4],[3,0],[1,13],[2,13],[6,0],[6,4],[0,13],[0,3],[7,4],[1,8],[5,5],[5,7],[5,10],[5,3],[6,10],[6,2],[3,10],[2,7],[1,12],[5,0],[4,5],[7,13],[3,2]]
n = 10
m = 17
operators = [[5,5],[0,7],[1,13],[5,14],[7,15],[3,15],[2,10],[4,6],[4,9],[1,2],[3,13],[4,8],[9,15],[6,4],[6,11],[9,11],[0,16],[3,6],[3,14],[6,1],[7,13],[2,0],[6,0],[6,9],[7,1],[7,4],[5,15],[0,1],[1,16],[6,16],[5,6],[3,12],[9,1],[7,2],[8,2],[6,2],[6,8],[4,7],[1,15],[3,0],[5,10],[9,9],[8,1],[8,4],[9,2],[3,11],[6,6],[2,16],[9,5],[2,4],[9,13],[3,16],[7,14],[2,3],[8,13],[7,10],[9,4],[8,16],[4,12],[3,2],[1,0],[1,9]]

Solution().numIslands2(n, m, operators)
