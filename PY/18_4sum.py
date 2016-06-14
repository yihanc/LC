# -*- coding: utf-8 -*- 
# 18. 4Sum My Submissions QuestionEditorial Solution
# Total Accepted: 74089 Total Submissions: 309004 Difficulty: Medium
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# 
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)
# Subscribe to see which companies asked this question
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        nums.sort()
        res = []
        
        for i in xrange(len(nums)-3):
            print ("-----" + str(i))
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1, len(nums)-2):
                print ("-----" + str(j))
            
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l < r:
                    print("----l ----- r" + str(l) + " " + str(r))
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    print("----- s: " + str(s))
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l, r = l+1, r-1
        
        return res

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        nums = [0,0,0,0]
        target = 0
        expected = [[0,0,0,0]]
        self.assertEqual(Solution().fourSum(nums, target), expected)
        
if __name__ == "__main__":
    unittest.main()
