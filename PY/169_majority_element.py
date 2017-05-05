# 169. Majority Element
# Description  Submission  Solutions  Add to List
# Total Accepted: 171120
# Total Submissions: 379446
# Difficulty: Easy
# Contributors: Admin
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.
# 
# Show Tags
# Show Similar Problems
# 

# 2017.04.30 
# Boyer-Moore Majority vote Algorithm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in xrange(1, len(nums)):
            if count == 0:
                major = nums[i]
                count = 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
        


#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        n = len(nums)
        for i in xrange(n):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if dic[nums[i]] > n / 2:
                return nums[i]

