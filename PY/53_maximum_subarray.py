# 53. Maximum Subarray  QuestionEditorial Solution  My Submissions
# Total Accepted: 136495
# Total Submissions: 360639
# Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# Subscribe to see which companies asked this question


# Solution
# 1. If curSum + nums[i] > 0, update curSum to the max of
# 2. else: reset curSum to nums[i] only
# 3. Update res with the max of (curSum, res)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        res, curSum = nums[0],  nums[0]
        
        for i in xrange(1, len(nums)):
            if curSum + nums[i] > 0:
                curSum = max(curSum+nums[i], nums[i])
            else:
                curSum = nums[i]
            res = max(res, curSum)

        return res
        

