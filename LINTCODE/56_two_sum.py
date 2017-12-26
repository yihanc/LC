# 56. Two Sum 
# 
# Given an array of integers, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.
# 
#  Notice
# 
# You may assume that each input would have exactly one solution
# 
# Have you met this question in a real interview? Yes
# Example
# numbers=[2, 7, 11, 15], target=9
# 
# return [1, 2]

# 2017.12.11
class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target-num], i]
            else:
                dic[num] = i
        return []
