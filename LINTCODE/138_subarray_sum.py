# 138. Subarray Sum 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.
# 
#  Notice
# 
# There is at least one subarray that it's sum equals to zero.
# 
# Have you met this question in a real interview? Yes
# Example
# Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

# 2017.12.11
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic = {0: -1}
        sum = 0
        for i, num in enumerate(nums):
            sum += num
            if sum in dic:
                return [dic[sum]+1, i]
            else:
                dic[sum] = i
        return []
