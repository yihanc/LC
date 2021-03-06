# 330. Patching Array Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 20824
# Total Submissions: 65643
# Difficulty: Hard
# Contributor: LeetCode
# Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.
# 
# Example 1:
# nums = [1, 3], n = 6
# Return 1.
# 
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.
# 
# Example 2:
# nums = [1, 5, 10], n = 20
# Return 2.
# The two patches can be [2, 4].
# 
# Example 3:
# nums = [1, 2, 2], n = 5
# Return 0.

# 20180113
# Assuming nothing in nums, to fill n = 100, we need, 1,2,4,8,16,32,64
# So we can see that patch are added in 2 's expo level
# If nums already had 7, 
# so we can see, we need everything before 7, 
# 1 2 4 7, we can reach, 1-7, 8,9,10,11,12,13,14 , but can't reach 15,
# so miss = 15, with patch 15, 1 2 4 7 15, now we can reach 15 + 14 = 29, but not 30
# so miss = 30, with patch 30, now we can reach 30 + 29 = 59
# so miss = 60, with patch 60, now we can reach 59 + 60 = 119
# so miss = 120, with patch 120
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, added, i = 1, 0, 0
        while miss <= n:
            print(miss, added, i)
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss <<= 1
                added += 1
        return added


# 2017.05.18
# Solution from Stefan Pochmann
## Explanation
## 
## Let miss be the smallest sum in [0,n] that we might be missing. Meaning we already know we can build all sums in [0,miss). Then if we have a number num <= miss in the given array, we can add it to those smaller sums to build all sums in [0,miss+num). If we don't, then we must add such a number to the array, and it's best to add miss itself, to maximize the reach.

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss, added, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and miss >= nums[i]:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                added += 1
        return added
                
                
                
