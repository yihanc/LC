# [35] 280    Wiggle Sort
# 
# 49.9%   Medium
# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]
# 
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
# 

# 2017.05.21
# wiggle sort ii solution
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = (len(nums) + 1) // 2
        #print(nums[mid:], nums[:mid])
        nums[::2], nums[1::2] = nums[:mid], nums[mid:]

class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(len(nums) - 1):
            if (( i % 2 == 0 and nums[i] > nums[i + 1] ) or 
                ( i % 2 == 1 and nums[i] < nums[i + 1] )):
                nums[i], nums[i+1] = nums[i+1], nums[i]


import random
if __name__ == "__main__":
    nums = [random.randint(0,20) for r in xrange(10)]
    # nums = [3, 5, 2, 1, 6, 4 ]
    Solution().wiggleSort(nums)
    print(nums)
    
