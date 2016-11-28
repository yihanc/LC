# 42. Trapping Rain Water My Submissions QuestionEditorial Solution
# Total Accepted: 68613 Total Submissions: 210598 Difficulty: Hard
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
# 
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
# 
# Subscribe to see which companies asked this question

# 11.25.2016 Rewrite
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2: return 0
        
        res = 0
        l, r = 0, n - 1
        lmax, rmax = height[0], height[n - 1]
        
        while l < r:
            if lmax < rmax:
                l += 1
                res += max(lmax - height[l], 0)
                lmax = max(lmax, height[l])
            else:
                r -= 1
                res += max(rmax - height[r], 0)
                rmax = max(rmax, height[r])
        return res
                
            


# Better. Two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r  = 0, n - 1
        leftMax, rightMax = 0, 0
        res = 0

        print(height)
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            print(" l: ", l, " r: ", r, " leftMax : ", leftMax, " rightMax : ", rightMax)
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
            else:
                res += rightMax - height[r]
                r -= 1

        return res

if __name__ == "__main__":
    b = [5,4,1,2]
#    print(Solution().trap(b))
#    a = [5,2,1,2,1,5]      # Top [5, 2, 5]
#    c = [5,5,1,7,1,1,5,2,7,6]
    d = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
#    e = [8,8,1,5,6,2,5,3,3,9]

    print(Solution().trap(d))


### Bad Solution. Too complicated
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        print(height)
        n = len(height)
        if n < 3:               # Bug 1
            return 0
        res = 0
        
        # Scan once to find top
        top = []
        for i in xrange(n):
            if ((i > 0 and i < n-1 and height[i] >= height[i-1] and height[i] >= height[i+1])
                or (i == 0 and height[i] >= height[i+1])
                or (i == n - 1 and height[i] >= height[i-1])):
                top.append(i)
        print(top)
        
        # 2. Scan again to filter some tops like [5, 2, 5]
        i = 1
        while i < len(top):
            if (i+1 < len(top) and height[top[i]] <= height[top[i-1]] 
                and height[top[i]] <= height[top[i+1]]):
                del top[i]
                continue
            i += 1
        print(top)
            
        # 3. Calculate water from founds tops
        for i in xrange(1, len(top)):
            lastTopI = top[i-1]
            curTopI = top[i]
            h = min(height[lastTopI], height[curTopI])
            res += h * (curTopI - lastTopI - 1)
            # minus shadow
            for j in xrange(lastTopI + 1, curTopI):
                res -= min(height[j], h)        # Bug 2, min
        
        return res
        

