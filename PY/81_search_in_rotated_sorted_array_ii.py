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
    
if __name__ == "__main__":
    print(Solution().search([1,3,1,1,1], 3))
