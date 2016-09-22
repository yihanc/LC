# 29. Divide Two Integers My Submissions QuestionEditorial Solution
# Total Accepted: 68030 Total Submissions: 432983 Difficulty: Medium
# Divide two integers without using multiplication, division and mod operator.
# 
# If it is overflow, return MAX_INT.
# 
# Subscribe to see which companies asked this question
#
# Analysis:
# 100 / 3
# divisor << 3, 6, 12, 24, 48, 96, 192(stop 192 > 100)
# dividend -= tmp << 1
#
# Corner Cases
# 1. -2147483648 / -1 , overflow, MAX_INT
# 2. divisor ==0, MAX_INT
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while dividend >= divisor:
            tmp = divisor
            count = 0
            while dividend >= tmp:
                tmp <<= 1
                count += 1
            dividend -= (tmp >> 1)
            res += (1 << (count-1))

        # Purely for OJ. since python don't overflow
        if res * sign > 2147483647:
            return 2147483647
        elif res * sign < -2147483648:
            return -2147483648
        else:
            return res * sign
                
if __name__ == "__main__":
    print(Solution().divide(-1,1))
    print(Solution().divide(100,3))
    print(Solution().divide(999,3))
    print(Solution().divide(300000,3))
