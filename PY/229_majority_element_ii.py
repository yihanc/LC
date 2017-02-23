# 229. Majority Element II
# Description  Submission  Solutions  Add to List
# Total Accepted: 47373
# Total Submissions: 169806
# Difficulty: Medium
# Contributors: Admin
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
# 
# Show Hint 
# 

# O(1) Space?
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        n = len(nums)
        for i in xrange(n):
            if nums[i] in dic and dic[nums[i]] == -1:
                continue
            else:
                dic[nums[i]] = dic.get(nums[i], 0) + 1
                if dic[nums[i]] > n / 3:
                    res.append(nums[i])
                    dic[nums[i]] = -1
                    
        return res
