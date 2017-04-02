# 283. Move Zeroes   QuestionEditorial Solution  My Submissions
# Total Accepted: 133653
# Total Submissions: 284077
# Difficulty: Easy
# Contributors: Admin
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# 
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

import random

# 2017.03.27 Rewrite
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n, j = 0, len(nums), 0
        while i < n and j < n:
            while i < n and nums[i] != 0: i += 1
            if j <= i: j = i + 1
            while j < n and nums[j] == 0: j += 1
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j + 1

# 2017.03.24 Cleaner and shorter code
# Find nums[i] == 0 and nums[j] != 0, swap and move i, j
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = -1
        for i in xrange(n):     # nums[i] == 0
            if nums[i] != 0: continue
            if j <= i: j = i + 1
                
            while j < n:        # nums[j] != 0
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j += 1
                
        return

# 2017.03.12 Swap solution (Much less operations than Sol2)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print("---- HERE -----")
        n = len(nums)
        l, cur = 0, 0
        count = 0
        print(nums)
        while l < n and cur < n:
            while l < n and nums[l] != 0:
                l += 1
                continue
            
            if l == n: 
                print("l == n ", n)
                return
            
            if cur <= l: cur = l + 1
            
            while cur < n and nums[cur] == 0:
                cur += 1
            
            if cur < n:
                count += 1
                nums[l], nums[cur] = nums[cur], nums[l]
            
        print("cur == n", count)
        return
          

# Bad solution. Much more operations
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        
        for num in nums:
            if num != 0:
                nums[i] = num
                count += 1
                i += 1
        
        while i < len(nums):
            nums[i] = 0
            count += 1
            i += 1

        print("sol2: ", count)



if __name__ == "__main__":
    nums1 = []
    nums2 = []

    for x in xrange(1000):
        nums1.append(random.sample(range(0, 3), 1)[0])
        nums2.append(random.sample(range(0, 3), 1)[0])

    print(nums1)
    Solution().moveZeroes(nums1)
    print(nums1)

    print("")

    print(nums2)
    Solution2().moveZeroes(nums2)
    print(nums2)
