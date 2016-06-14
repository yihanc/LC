# 16. 3Sum Closest My Submissions QuestionEditorial Solution
# Total Accepted: 79046 Total Submissions: 269938 Difficulty: Medium
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
#     For example, given array S = {-1 2 1 -4}, and target = 1.
# 
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Subscribe to see which companies asked this question

# Same idea as 3 sum. Change 0 to target and update res everytime
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sys.maxint
        
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(res-target) > abs(s - target):
                    res = s
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l, r = l+1, r-1
        return res
