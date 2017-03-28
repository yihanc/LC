# 35. Search Insert Position My Submissions QuestionEditorial Solution
# Total Accepted: 107798 Total Submissions: 286774 Difficulty: Medium
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

# 2017.03.24 Binary search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if ( (mid == 0 and target <= nums[mid])
                or (mid != 0 and nums[mid - 1] < target <= nums[mid]) ):
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

# 11.20.2016
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            if l == r and target <= nums[l]:
                return l
            if l == r and target > nums[l]:
                return l + 1
            
            mid = (l + r) // 2
            
            if target <= nums[mid] and (mid == 0 or (mid > 0 and target > nums[mid-1])):
                return mid
            
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        
        start, end = 0, len(nums) - 1
        while start < end:
            if target <= nums[start]:
                return start
            elif nums[end] < target:
                return end + 1
            elif nums[end] == target:
                return end
                
            mid = start + ( end - start ) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        if target <= nums[start]:
            return start
        else:
            return start + 1


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid] and (target > nums[mid-1] or mid == l):
                return mid
            elif target > nums[mid] and (target < nums[mid+1] or mid == r):
                return mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        if target <= nums[l]: return l
        else: return l + 1
