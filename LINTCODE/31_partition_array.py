# 31. Partition Array 
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
# 
# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.
# 
#  Notice
# You should do really partition in array nums instead of just counting the numbers of integers smaller than k.
# 
# If all elements in nums are smaller than k, then return nums.length
# 
# Have you met this question in a real interview? Yes
# Example
# If nums = [3,2,2,1] and k=2, a valid answer is 1.

        
class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums: return 0
        if len(nums) == 1:
            if nums[0] < k: return 1
            else: return 0
            
        l, r, cur = 0, len(nums) - 1, 0
        while l < r and cur < len(nums):
            if l < r and nums[l] < k:    
                l += 1
                if cur < l: cur = l
                continue
            
            if l < r and nums[r] >= k:
                r -= 1
                continue
            
            if nums[cur] < k and cur != l:
                nums[l], nums[cur] = nums[cur], nums[l]
                l += 1
                cur += 1
                continue
            
            if nums[cur] >= k and cur != r:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
                continue
            cur += 1
        return l if nums[l] >= k else l + 1

# nums = [3,2,2,1]
nums = [7,7,9,8,6,6,8,7,9,8,6,6]
print(Solution().partitionArray(nums, 10))

