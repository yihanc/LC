# 69. Sqrt(x)  QuestionEditorial Solution  My Submissions
# Total Accepted: 111505
# Total Submissions: 424137
# Difficulty: Medium
# Implement int sqrt(int x).

#11.27.2016 Newton's
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: return -1

        r = x
        while r * r > x:
            r = (r + x / r) / 2
            
        return r

import sys 

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
    
        start, end = 0, sys.maxint
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid <= x and x < (mid + 1) * (mid +1):
                return mid
            elif x < mid * mid:
                end = mid - 1
            else:
                start = mid + 1

if __name__ == "__main__":
    print(Solution().mySqrt(0))
    print(Solution().mySqrt(1))
    print(Solution().mySqrt(2))
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(8))
    print(Solution().mySqrt(16))
