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
        # Sign
        sign = True
        if dividend > 0 and divisor < 0 or (dividend < 0 and divisor > 0):
            sign = False
            
        # MAXINT
        MAX_INT, MIN_INT = 2147483647, -2147483648
        
        # Special Case
        if divisor == 0 or (dividend == MIN_INT and divisor == -1): 
            return MAX_INT
        
        #
        res = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            count, tmp = 0, divisor
            while dividend >= tmp:
                tmp <<= 1
                count += 1
            tmp >>= 1
            if count > 0: count -= 1
            dividend -= tmp
            res += (1 << count)
            
        if sign: return res
        else: return 0 - res

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        A = Solution().divide(100, 3)
        B = 33
        self.assertEqual(A, B)
    
    def test_1(self):
        A = Solution().divide(0, 3)
        B = 0
        self.assertEqual(A, B)

    def test_2(self):
        A = Solution().divide(4, 3)
        B = 1
        self.assertEqual(A, B)

    def test_3(self):
        A = Solution().divide(4, 0)
        B = 2147483647
        self.assertEqual(A, B)

    def test_4(self):
        A = Solution().divide(10003, 5)
        B = 2000
        self.assertEqual(A, B)

    def test_5(self):
        A = Solution().divide(10003, 0)
        B = 2147483647
        self.assertEqual(A, B)

    def test_6(self):
        A = Solution().divide(-2147483648, -1)
        B = 2147483647
        self.assertEqual(A, B)

if __name__ == "__main__":
    unittest.main()
