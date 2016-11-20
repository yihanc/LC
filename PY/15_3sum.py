# # 15. 3Sum My Submissions QuestionEditorial Solution
# Total Accepted: 119433 Total Submissions: 630217 Difficulty: Medium
# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
# 
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)
# Subscribe to see which companies asked this question

# 11.19.2016
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        
        nums.sort()
        
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                
                if k + 1 < len(nums) and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
            i += 1
            
        return res
        
        

class Solution(object):
    # i from 0 to len(nums) - 2
    # l = i + 1, r from len(nums) -1 
    # Handling duplicates
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  #Removing i duplicate
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:   #Removing l duplicate
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   #Removing r duplicate
                        r -= 1
                    l, r = l+1, r-1
            
        return res
            
import unittest
class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_1(self):
        self.assertEqual(Solution().threeSum([0, 0, 0, 0]), [[0, 0, 0]])

    def test_2(self):
        self.assertEqual(Solution().threeSum([0, 0, 0, 0, 0]), [[0, 0, 0]])

    def test_3(self):
        self.assertEqual(Solution().threeSum([0, 0]), [])

    def test_4(self):
        self.assertEqual(Solution().threeSum([0]), [])

    def test_5(self):
        self.assertEqual(Solution().threeSum([]), [])

    def test_6(self):
        self.assertEqual(Solution().threeSum([1, -1, -1, 0]), [[-1, 0, 1]])

if __name__ == "__main__":
    unittest.main()
    #(Solution().threeSum([3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]))
