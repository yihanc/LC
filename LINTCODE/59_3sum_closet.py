# 59. 3Sum Closest 
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.
# 
#  Notice
# You may assume that each input would have exactly one solution.
# 
# Have you met this question in a real interview? Yes
# Example
# For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 3: raise Exception("No answer")
        res = numbers[0] + numbers[1] + numbers[2]
        numbers.sort()
        i = 0
        while i < len(numbers) - 2:
            if i > 0 and numbers[i] == numbers[i-1]:
                i += 1
                continue
            
            l, r = i + 1, len(numbers) - 1
            while l < r:
                if l > i + 1 and numbers[l] == numbers[l-1]:
                    l += 1
                    continue
                
                if r < len(numbers) - 1 and numbers[r] == numbers[r+1]:
                    r -= 1
                    continue
                
                sum = numbers[i] + numbers[l] + numbers[r]
                if abs(sum - target) < abs(res - target): res = sum
                    
                if sum == target: return sum
                elif sum > target: r -= 1
                else: l += 1
                    
            i += 1
        return res
