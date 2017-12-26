# 14. First Position of Target 
# For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.
# 
# If the target number does not exist in the array, return -1.
# 
# Have you met this question in a real interview? Yes
# Example
# If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if not nums or len(nums) == 0: return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid] and (mid == 0 or nums[mid] != nums[mid - 1]):
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l if nums[l] == target else -1
