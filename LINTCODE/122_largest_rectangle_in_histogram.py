

# 12.30.2017

from collections import deque
class Solution:
    """
    @param: height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        if not height or len(height) == 0: return 0
        
        height.append(0)
        d = deque()
        res = 0
        
        for i in xrange(len(height)):
            while d and height[d[-1]] > height[i]:
                h = height[d.pop()]
                left = d[-1] if d else -1
                res = max(res, (i - left - 1) * h)
            d.append(i)
        return res
            
