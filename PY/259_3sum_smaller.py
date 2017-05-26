# 259. 3Sum Smaller Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23955 Total Submissions: 58266 Difficulty: Medium Contributor: LeetCode
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# 
# For example, given nums = [-2, 0, 1, 3], and target = 2.
# 
# Return 2. Because there are two triplets which sums are less than 2:
# 
# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

# 2017.05.23
# 3 pointers
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return 0
        res = 0
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[i] + nums[j] + nums[k]
                if cur < target:
                    res += k - j        # Key point
                    j += 1
                else:
                    k -= 1
            i += 1
        return res
            
        
