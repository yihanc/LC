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

# 2017.03.04 My style. l < r
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]


# 2017.02.25 Better. Always compare with the right
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
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            

# 2017.02.25 Rewrite
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
            print(l, r, mid, nums[mid])
            if ((mid == 0 or nums[mid] < nums[mid - 1]) 
                and (mid == n - 1 or nums[mid] < nums[mid + 1])):
                return nums[mid]
            elif (nums[mid] < nums[l] or (nums[l] < nums[mid] and nums[l] < nums[r])):
                r = mid - 1
            else:
                l = mid + 1
        
                

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
