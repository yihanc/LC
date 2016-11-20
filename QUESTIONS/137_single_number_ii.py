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
        A = {}
        for num in nums:
            if num in A:
                A[num] += 1
            else:
                A[num] = 1
        print(A)
        
        for key in A:
            if A[key] == 1:
                return key

if __name__ == "__main__":
    print(Solution().singleNumber([1]))
