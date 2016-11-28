# 34. Search for a Range My Submissions QuestionEditorial Solution
# Total Accepted: 85406 Total Submissions: 290788 Difficulty: Medium
# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
# 
# Subscribe to see which companies asked this question

# 11.20.2016
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1, -1]

        l, r = 0, n -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                res[0] = mid
                break
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target and (mid == n - 1 or nums[mid+1] != target):
                res[1] = mid
                break
            
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return res
            
            

class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [ -1, -1 ]
        
        res = [ -1, -1 ]
        # Search left end
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target and ( mid - 1 < 0 or nums[mid-1] != nums[mid] ):
                res[0] = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        # Search right end
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target and (mid + 1 == len(nums) or nums[mid+1] != nums[mid] ):
                res[1] = mid
                return res
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return res

# Test case
# [0] 1
# [0] 0
# [0, 0] 0
# [ 0, 1, 3, 4, 5, 7, 7, 8]
        


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        l, r = 0, len(nums)-1

        # Search left range
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid] and (mid == l or nums[mid] != nums[mid - 1]):
                res[0] = mid
                break
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        if res[0] == -1 and nums[l] == target: res[0] = l
            
        print (res)
        # Search right end
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            print(mid)
            if target == nums[mid] and (mid == r or nums[mid] != nums[mid + 1]):
                res[1] = mid
                break
            elif target >= nums[mid]:   # Search right half
                l = mid + 1
            else:
                r = mid - 1

        if res[1] == -1 and nums[l] == target: res[1] = l
        print(res)

        return res

import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])

if __name__ == "__main__":
    unittest.main()
