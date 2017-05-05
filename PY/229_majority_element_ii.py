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

# 2017.05.01 voting algorithms
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        can1, can2, count1, count2 = None, None, 0, 0
        
        for num in nums:
            #print(can1, can2, count1, count2)
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1, count1 = num, 1
            elif count2 == 0:
                can2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        return [ x for x in [can1, can2] if nums.count(x) > len(nums) / 3]
        

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
