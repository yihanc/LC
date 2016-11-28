# 153. Find Minimum in Rotated Sorted Array  QuestionEditorial Solution  My Submissions
# Total Accepted: 111472
# Total Submissions: 295421
# Difficulty: Medium
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Subscribe to see which companies asked this question

# 11.20.2016 
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if (l == r or (mid > 0 and nums[mid-1] > nums[mid])
                or (mid == 0 and nums[mid] < nums[r])):
                return nums[mid]
            
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1


class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + ( end - start ) // 2
            #1. mid < mid -1; 2. mid == 0 and mid <=j
            if (( mid > 0 and nums[mid - 1] > nums[mid] ) or
                ( mid == start and nums[mid] <= nums[end] )or
                start == end ): 
                return nums[mid]
            # Search left when mid < end
            elif nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1

        return nums[start]

# Test cases
# 1 2
# 2 1
# 0 1 2 3 4 5 6 7
# 7 0 1 2 3 4 5 6
# 1 2 3 4 5 6 7 0
# 2 3 4 5 6 7 0 1
# 6 7 0 1 2 3 4 5
