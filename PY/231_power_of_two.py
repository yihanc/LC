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

# 2017.04.20
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >= 1 and n & ( n - 1) == 0


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
