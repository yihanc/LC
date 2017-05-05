# 137. Single Number II  QuestionEditorial Solution  My Submissions
# Total Accepted: 98617
# Total Submissions: 250008
# Difficulty: Medium
# Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# 2017.04.23 General Method
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for c in nums:
            a, b = (a&~b&~c)|(~a&~b&c), (~a&b&~c)|(a&~b&c)        
        return a | b

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for num in nums:
            tmp = (a & ~b & ~num) + (~a & ~b & num)
            b = (~a & b & ~num) + (a & ~b & num)
            a = tmp
        return a | b

if __name__ == "__main__":
    Solution().singleNumber([4,5,4,4])
