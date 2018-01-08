class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0: return 0
        cur = res = nums[0]
        
        for i in xrange(1, len(nums)):
            cur = max(cur + nums[i], nums[i])
            res = max(res, cur)
        return res
