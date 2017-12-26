# 50. Product of Array Exclude Itself 
#  Description
#  Notes
#  Testcase
#  Judge
# Given an integers array A.
# 
# Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.
# 
# Have you met this question in a real interview? Yes
# Example
# For A = [1, 2, 3], return [6, 3, 2].
# 
# 

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        if not nums or len(nums) == 0: return []
        if len(nums) == 1: return [1]
        res = [1] * len(nums)
        i = 1
        while i < len(nums):
            res[i] *= res[i-1] * nums[i-1]
            i += 1
        
        i, tmp = len(nums) - 2, 1
        while i >= 0:
            tmp *= nums[i+1]
            res[i] *= tmp
            i -= 1
        return res
