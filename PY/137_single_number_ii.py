# 137. Single Number II  QuestionEditorial Solution  My Submissions
# Total Accepted: 98617
# Total Submissions: 250008
# Difficulty: Medium
# Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        a, b = 0, 0
        for num in nums:
	    print(bin(a), bin(b), bin(num))
            a, b = (a&~b&~num)|(~a&b&num), (~a&b&~num)|(~a&~b&num)
        
        print(bin(a), bin(b), bin(num))
        print("res: ", a|b)
        return a|b


if __name__ == "__main__":
    Solution().singleNumber([4,5,4,4])
