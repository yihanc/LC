# 152. Maximum Product Subarray My Submissions QuestionEditorial Solution
# Total Accepted: 60873 Total Submissions: 271144 Difficulty: Medium
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
# Subscribe to see which companies asked this question

# Record max and min.
# If < 0, mx = last max and min * cur)
# if > 0, mx = 
# DP
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        cur_max = cur_min = res = nums[0]
        
        i = 1
        while i < len(nums):
            tmp_max = max(nums[i],  max(cur_max * nums[i], cur_min * nums[i]))
            tmp_min = min(nums[i],  min(cur_max * nums[i], cur_min * nums[i]))
            cur_max, cur_min = tmp_max, tmp_min
            res = max(res, cur_max)
            i += 1
        return cur_max

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual( Solution().maxProduct([-4,-3,-2]), 12 )
        self.assertEqual( Solution().maxProduct([-2,0,-1]), 2)

if __name__ == "__main__":
    unittest.main()
