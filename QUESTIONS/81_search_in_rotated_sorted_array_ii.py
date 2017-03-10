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
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

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
    
