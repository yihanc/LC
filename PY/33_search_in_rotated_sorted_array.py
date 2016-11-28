# 33. Search in Rotated Sorted Array My Submissions QuestionEditorial Solution
# Total Accepted: 104226 Total Submissions: 341737 Difficulty: Hard
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Subscribe to see which companies asked this question

# 11.20.2016. Rewrite
# Algorithm:
# while l <= r, 
# if nums[mid] == target, return
# For the following two scenarios, when to search left, when to search right
# 1. nums[mid] > nums[l]
# 2. nums[mid] < nums[l]
# If not loop, return - 1
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if ((nums[mid] < nums[l] and ( target >= nums[l] or target < nums[mid]))
                or (nums[mid] > nums[l] and target < nums[mid] and target >= nums[l])) :
                r = mid - 1
            else:
                l = mid + 1

        return -1
        

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            # Key Part. Note that ">=" for nums[0]
            elif (( target < nums[mid] and target >= nums[0] )
                or ( nums[0] > nums[mid] and (target >= nums[0] or target < nums[mid])) ):
                end = mid - 1
            else:
                start = mid + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([0], 0))
    print(sol.search([0], 1))
    print(sol.search([0,1], 0))
    print(sol.search([0,1], 1))
    print(sol.search([0,1], 2))
    print(sol.search([1,0], 0))
    print(sol.search([1,0], 1))
    print(sol.search([1,0], 2))
    print(sol.search([2,3,1], 2))
    print(sol.search([2,3,1], 3))
    print(sol.search([2,3,1], 1))
    print(sol.search([2,3,1], 4))
    print(sol.search([3,1,2], 3))
    print(sol.search([3,1,2], 1))
    print(sol.search([3,1,2], 2))
    print(sol.search([3,1,2], 4))
    print(sol.search([1,2,3], 1))
    print(sol.search([1,2,3], 2))
    print(sol.search([1,2,3], 3))
    print(sol.search([1,2,3], 4))

# Test cases
# [0] 1
# [0 1] -1
# [0 1] 1
# [1 0] 2
# [1 0] 0
# [1 0] 1
# [2, 3, 1] 2
# [3, 1, 2] 3
# [1, 2, 3] 1
# 0 1 2 3 4 5 6 7
# 6 7 0 1 2 3 4
# 7 0 2 4 5 6 
# 5 6 7 8 0 1 2
