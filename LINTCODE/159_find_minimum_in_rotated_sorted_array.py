class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums or len(nums) == 0: raise Exception("Input is not valid")
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if (( mid == 0 or nums[mid] < nums[mid - 1]) and
                (mid == len(nums) - 1 or nums[mid] < nums[mid + 1])):
                return nums[mid]
            elif nums[mid] < nums[-1]:
                r = mid - 1
            else:
                l = mid + 1
        
        
