# 324. Wiggle Sort II Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 25478
# Total Submissions: 100058
# Difficulty: Medium
# Contributors: Admin
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# 
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = (len(nums) - 1) // 2
        print(nums[::2])
        print(nums[1::2])
        print(nums[:half:-1], nums[half::-1])
        print(nums[::-1])
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

if __name__ == "__main__":
    # nums = [1,1,2,1,2,2,1]
    nums = [1,5,1,1,6,4]
    Solution().wiggleSort(nums)
    print("END: ", nums)
