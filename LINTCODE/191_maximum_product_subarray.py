class Solution:
    """
    @param: nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums or len(nums) == 0: return 0
        res = cur_max = cur_min = nums[0]
        
        for i in xrange(1, len(nums)):
            if nums[i] > 0:
                cur_max, cur_min = max(cur_max * nums[i], nums[i]), min(cur_min * nums[i], nums[i])
            else:
                cur_max, cur_min = max(cur_min * nums[i], nums[i]), min(cur_max * nums[i], nums[i])
            res = max(cur_max, res)
        return res
                
            
