# 80. Remove Duplicates from Sorted Array II   QuestionEditorial Solution  My Submissions
# Total Accepted: 94370
# Total Submissions: 274007
# Difficulty: Medium
# Contributors: Admin
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        n = len(nums)
        char = ""
        count = 0
        i = 0
        while i < len(nums):
            if i == 0 or nums[i] != nums[i-1]:
                char = nums[i]
                count = 1
                i += 1
                continue
        
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    del nums[i]
                    continue
                i += 1
        print(nums)
        return len(nums)
                
if __name__ == "__main__":
    nums = [1,1,1,1,1,1,1,2,2,3]
    Solution().removeDuplicates(nums)
