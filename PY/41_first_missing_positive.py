# 41. First Missing Positive My Submissions QuestionEditorial Solution
# Total Accepted: 66114 Total Submissions: 275421 Difficulty: Hard
# Given an unsorted integer array, find the first missing positive integer.
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# Your algorithm should run in O(n) time and uses constant space.

# 2018.02.19
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = set(nums)
        i = 1
        while i in S:
            i += 1
        return i


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            while nums[i] >= 1 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                print("i: ", i, " nums[i]: ", nums[i], " nums[nums[i]-1]: ", nums[nums[i]-1]) 
                tmp = nums[i]-1     # Bug if no this line
                nums[i], nums[tmp] = nums[tmp], nums[i]
        
        for i in xrange(n):
            if nums[i] != i+1:
                return i+1
        return n+1

if __name__ == "__main__":
    print(Solution().firstMissingPositive([2,1]))
