# 题1
# Given an array with non negative numbers, divide the array into two parts 
# such that the average of both the parts is equal.
# Return both parts (If exist).
# If there is no solution. return an empty list.
# 
# Example:
# 
# 
# Input:
# [1 7 15 29 11 9]
# 
# Output:
# [9 15] [1 7 11 29]
# 
# The average of part is (15+9)/2 = 12,
# average of second part elements is (1 + 7 + 11 + 29) / 4 = 12
class Solution(object):
    def divideArrayAvg(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        self.unittest.assertEqual(Solution().divideArrayAvg([1, 7, 15, 29, 11, 9]), [[9, 15], [1, 7, 11, 29])

if __name__ == "__main__":
    unittest.main()
