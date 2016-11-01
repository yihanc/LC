# 75. Sort Colors   QuestionEditorial Solution  My Submissions
# Total Accepted: 125477
# Total Submissions: 346437
# Difficulty: Medium
# Contributors: Admin
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note:
# You are not suppose to use the library's sort function for this problem.
# 
# click to show follow up.
# 
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# 
# Could you come up with an one-pass algorithm using only constant space?
# Subscribe to see which companies asked this question
import random
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 3:
            return
        
        l, r = 0, n-1

        while l < r:
            while nums[l] == 0:
                l += 1
        
            while nums[r] == 2:
                r -= 1
                
            if nums[l] == 2 and nums[r] == 0:
                nums[l], nums[r] = 0, 2
                l, r = l+1, r-1
                continue

            mid = l + 1
            while mid != r and nums[mid] == 1:
                mid += 1

            if mid >= r:
                break   # QUIT LOOP. All sorted

            if mid == 0:    # swap l
                tmp = nums[l]
                nums[l] = nums[mid]
                nums[mid] = tmp
                l += 1
                continue
            if mid == 2:    # swap r
                tmp = nums[r]
                nums[r] = nums[mid]
                nums[mid] = tmp
                r -= 1
                continue


if __name__ == "__main__":
    nums = [] 
    for i in xrange(3):
        nums.append(random.randint(0,2))

    print(nums)
    Solution().sortColors(nums)
    print("---finished----")
    print(nums)
