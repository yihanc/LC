class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if not nums or len(nums) == 0: return []
        if len(nums) == 1: return nums
        
        i = len(nums) - 1
        while i >= 0:
            if nums[i] > nums[i - 1]:
                i -= 1
                break
            i -= 1
        
        if i == -1: return sorted(nums)
        
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        return nums[:i+1] + sorted(nums[i+1:])
