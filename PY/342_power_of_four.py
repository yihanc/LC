# 342. Power of Four
# Description  Submission  Solutions  Add to List
# Total Accepted: 53560
# Total Submissions: 142407
# Difficulty: Easy
# Contributors: Admin
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# 
# Example:
# Given num = 16, return true. Given num = 5, return false.
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:
# Special thanks to @yukuairoy for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 0x55555555 to get rid of power of 2 but leave power of 4
        return num >= 1 and (num & (num - 1) == 0) and (num & 0x55555555 != 0)
        


# 2017.04.22
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 1
        while n < num:
            n = n << 2
        return n == num



class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        while start < num:
            start = start * 4
        return start == num
        
