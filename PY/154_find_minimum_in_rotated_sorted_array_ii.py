# 154. Find Minimum in Rotated Sorted Array II  QuestionEditorial Solution  My Submissions
# Total Accepted: 60796
# Total Submissions: 171004
# Difficulty: Hard
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.

# 2017.03.04 l < r style
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

# Better solution online.
# Always compare with the nums[r]
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            if l == r: return nums[l]
            
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        

# Similar to 153. Handle duplicates
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            if l == r:
                return nums[l]
                
            mid = (l + r) // 2
            
            if nums[mid] == nums[r]:
                r -= 1
                continue
            
            if nums[l] == nums[r]:
                l += 1
                continue
            
            if ((mid > 0 and nums[mid-1] > nums[mid])
                or (mid == 0 and nums[mid] < nums[r])):
                return nums[mid]
            
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            if l < r and nums[l] == nums[r] :
                r -= 1

            if nums[l] < nums[r] or l == r:
                return nums[l]

            mid = l + (r - l) // 2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
