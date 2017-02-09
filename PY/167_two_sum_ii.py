# 167. Two Sum II - Input array is sorted
# Description  Submission  Solutions  Add to List
# Total Accepted: 52628
# Total Submissions: 109210
# Difficulty: Easy
# Contributors: Admin
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
# Subscribe to see which companies asked this question.
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        res = [None, None]
        i, j = 0, n - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                res[0], res[1] = i + 1, j + 1
                return res
            elif sum > target:
                j -= 1
            else:
                i += 1
        

