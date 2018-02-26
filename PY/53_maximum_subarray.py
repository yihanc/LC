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

# 2018.02.21
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res, csum = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            csum = max(csum + nums[i], nums[i])
            res = max(res, csum)
        return res
            

# 11.26.2016. Rewrite
# Algorithm:
# Traverse the list
# 1. Update curMax. curMax = max(nums[i], curMax + nums[i])
# 2. Update preMax. preMax = max(preMax, curMax)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        preMax, curMax = nums[0], nums[0]
        
        for i in xrange(1, n):
            curMax = max(nums[i], curMax + nums[i])
            preMax = max(preMax, curMax)
        
        return preMax


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
        

