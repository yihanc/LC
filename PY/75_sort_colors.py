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

# 12.24.2016 Rewrite. Dutch Flag standard template

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l, i = l + 1, i + 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1

import random

# Rewrite. two pointers. 
# Note: cur pointer should include both l and r.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
    
        l, r = 0, n - 1
        
        cur = 0
        while cur <= r and l < r:       # Trick. cur should include l and r
            if nums[l] == 0: 
                l += 1
                continue
            
            if nums[r] == 2:
                r -= 1
                continue
            
            if cur < l:
                cur = l
            
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
            elif nums[cur] == 2:
                nums[r], nums[cur] = nums[cur], nums[r]
                r -= 1
            else:
                cur += 1
                
        return

class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return

        l, r = 0, n-1
        cur = 0
        while cur <= r:     # N1. cur from 0 to r, inclusive
            print(nums)
            print(str(l) + " " + str(cur) + " " + str(r))
            if nums[cur] == 0:
                nums[l], nums[cur] = nums[cur], nums[l]
                l, cur = l+1, cur+1 
            elif nums[cur] == 2:        # If cur == 2, don't change cur.
                nums[r], nums[cur] = nums[cur], nums[r] 
                r -= 1
            else:
                cur += 1


if __name__ == "__main__":
    nums = [] 
    for i in xrange(10):
        nums.append(random.randint(0,2))

#    nums = [2, 0, 2, 0, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 0, 0, 2, 2, 2, 2]
#    nums = [1, 1, 2, 2, 1, 0, 0, 2, 2, 0, 2, 1, 0, 2, 0, 0, 2, 0, 1, 0]
#    nums = [0, 0, 0]
#    nums = [2, 2, 2]

    print(nums)
    Solution().sortColors(nums)
    print("---finished----")
    print(nums)
