# 50. Pow(x, n)  QuestionEditorial Solution  My Submissions
# Total Accepted: 109174
# Total Submissions: 398298
# Difficulty: Medium
# Implement pow(x, n).
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1.0 / x
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

if __name__ == "__main__":
    print(Solution().myPow(5,1))
    print(Solution().myPow(5,-1))
    print(Solution().myPow(5,-2))
    print(Solution().myPow(5,-3))
    print(Solution().myPow(2,2))
    print(Solution().myPow(2,3))
    print(Solution().myPow(2,4))
    print(Solution().myPow(2,6))
    print(Solution().myPow(2,9))
    print(Solution().myPow(2,10))
        
