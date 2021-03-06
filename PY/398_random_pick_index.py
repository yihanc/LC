# 398. Random Pick Index Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 16802
# Total Submissions: 40405
# Difficulty: Medium
# Contributor: LeetCode
# Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
# 
# Example:
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return random.choice([i for i in xrange(len(self.nums)) if self.nums[i] == target])
