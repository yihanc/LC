# 231. Power of Two
# Description  Submission  Solutions  Add to List
# Total Accepted: 120547
# Total Submissions: 305767
# Difficulty: Easy
# Contributors: Admin
# Given an integer, write a function to determine if it is a power of two.
# 
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        start = 1
        while start < n:
            start = start * 2
        return start == n
