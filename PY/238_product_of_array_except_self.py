# 238. Product of Array Except Self Add to List
# Description  Submission  Solutions
# Total Accepted: 84886
# Total Submissions: 178017
# Difficulty: Medium
# Contributors: Admin
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
# 
# Subscribe to see which companies asked this question.
# 

# Two passes
# 1. Left to right. res[i] = Multiply of (res[:i])
# 2. Right to left. res[i] = Multiply of (res[i-1:]
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [ 0 for x in xrange(n) ]
        res[0] = 1
        for i in xrange(1, n):
            res[i] = res[i-1] * nums[i-1]

        print(res)
        right = 1
        for i in xrange(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
            print(right)

        print(res)
        return res
        

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))
