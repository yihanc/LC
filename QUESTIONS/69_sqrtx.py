# 69. Sqrt(x)  QuestionEditorial Solution  My Submissions
# Total Accepted: 111505
# Total Submissions: 424137
# Difficulty: Medium
# Implement int sqrt(int x).
import sys 

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x
        while y * y > x:
            print(y, x)
            y = ( y + x / y ) / 2
        
        return y

if __name__ == "__main__":
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(8))
    print(Solution().mySqrt(16))
    print(Solution().mySqrt(100))
    print(Solution().mySqrt(500))
    print(Solution().mySqrt(1000))
    print(Solution().mySqrt(2147483648))
