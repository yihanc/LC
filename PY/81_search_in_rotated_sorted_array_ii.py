# 81. Search in Rotated Sorted Array II My Submissions QuestionEditorial Solution
# Total Accepted: 64253 Total Submissions: 200316 Difficulty: Medium
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# 
# Would this affect the run-time complexity? How and why?
# 
# Write a function to determine if a given target is in the array.
# 
# Subscribe to see which companies asked this question

# 2017.03.04 Rewrite in my style
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            elif ((nums[mid] > nums[r] and (target > nums[mid] or target <= nums[r]))
                or (nums[mid] < nums[r] and target > nums[mid] and target <= nums[r])):
                l = mid + 1
            else:
                r = mid - 1
            
        return l if nums[l] == target else -1
        

# 2017.02.25 One template for all.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            if l == r and nums[l] != target:
                return False
            
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[r]:
                r -= 1
            elif (( nums[mid] < nums[r] and target > nums[mid] and target <= nums[r] )
                or ( nums[mid] > nums[r] and (target > nums[mid] or target <= nums[r]))):
                l = mid + 1
            else:
                r = mid

# Similar to Question 33
# Only check nums[l] and nums[r]
# Case 1: 012345678
# Case 2: 780123456
# When to go r = mid - 1?
# In case 1, target >= nums[l] and target < nums[r]
# In case 2 nums[l] > nums[mid], target > nums[l] or target < nums[mid] 
# When to l = mid + 1? else


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
                
            if nums[l] == nums[mid]:
                l += 1
                continue

            if ( ( target < nums[mid] and target >= nums[l] ) or
                ( nums[l] > nums[mid] and ( target >= nums[l] or target < nums[mid] ))):
                r = mid - 1
            else:
                l = mid + 1
        
        return False

# Similar to 33. Handle duplicates
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if not nums: return -1
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            if nums[l] == nums[r] or nums[l] == nums[mid]:
                l += 1
                continue
            
            if nums[r] == nums[mid]:
                r -= 1
                continue
                
            if ((nums[mid] < nums[l] and (target >= nums[l] or target < nums[mid]))
                or (nums[mid] > nums[l] and target >= nums[l] and target < nums[mid])):
                r -= 1
            else:
                l += 1
        
        return False

class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
    
        start, end = 0, len(nums) - 1
        while start <= end:
            # Remove duplicates for left end
            while start < end and nums[end] == nums[end - 1]:
                end -= 1
            while start < end and nums[start] == nums[start + 1]:
                start += 1
            if nums[start] == nums[end] and start != end:
                end -= 1

            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True
            elif (( target < nums[mid] and target >= nums[0] ) or
                  ( nums[mid] < nums[0] and (target >= nums[0] or target < nums[mid])) ):
                end = mid - 1
            else:
                start = mid + 1
        
        return False

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

if __name__ == "__main__":
    print(Solution().search([1,3,1,1,1], 3))
    print(Solution().search([1,1,1,3,1], 3))
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



















class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2      # Python don't overflow

            while nums[l] == nums[mid] and mid - 1 > l: # Remove duplicates from the left side
                mid = mid - 1                           # Worst case o(n)
            
            if target == nums[mid]:
                return True
            elif target == nums[l]:
                return True
            elif target == nums[r]:
                return True
                
            if ((target > nums[l] and target < nums[mid]) or
                (nums[l] > nums[mid] and ( target > nums[l] or target < nums[mid]))):
                r = mid - 1
            else:
                l = mid + 1
                
        if target == nums[l]: return True
        else: return False
    
