# 55. Jump Game  QuestionEditorial Solution  My Submissions
# Total Accepted: 93629
# Total Submissions: 323161
# Difficulty: Medium
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# A = [3,2,1,0,4], return false.
# 
# Subscribe to see which companies asked this question

# One loop. O(1) solution
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = 0
        for i in xrange(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True

# DP solution get a TLE
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        n = len(nums)
        print("n : " + str(n))
        res = [False for x in xrange(n)]
        
        res[-1] = True
        print(res)
        
        for i in reversed(xrange(0, n-1)):
            print("i : " + str(i))
            print(res)
            j = nums[i]
            print("j : " + str(j))
            if i + j >= n - 1:
                res[i] = True
                continue
            
            while j > 0:
                if res[i+j]:
                    res[i] = True
                    break
                j -= 1

        print(res)

        return res[0]

if __name__ == "__main__":
    A = [1, 2]
    Solution().canJump(A)
