# 60. Permutation Sequence   QuestionEditorial Solution  My Submissions
# Total Accepted: 68146
# Total Submissions: 255846
# Difficulty: Medium
# Contributors: Admin
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.
# 
# Subscribe to see which companies asked this question

# 11.27.2016 Rewrite
# Bug notes: 
# 1. import math for factorial. otherwise write a function
# 2. k = (k - 1) % tmp + 1
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n <= 0 or k <= 0: return ""
        
        res = ""
        nums = [ x for x in xrange(1, n+1) ]
        
        while n > 1:
            tmp = math.factorial(n-1)  # 2 
            i, k = (k - 1) // tmp, (k - 1) % tmp + 1    # k = (k - 1) % tmp + 1 bug
            res += str(nums[i])
            del nums[i]
            n -= 1
        
        return res + str(nums[0])











# Sol 2 TLE
class Solution2(object):
    count = 0
    res = ""
    resFound = False
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [ str(x) for x in xrange(1,n+1)]
        self.dfs("", nums, k)
        return self.res

    def dfs(self, line, nums, k):
        if self.resFound:
            return 
        
        if not nums:
            self.count += 1
            if self.count == k:
                self.res = line
                self.resFound = True
            return 
        
        for i in xrange(len(nums)):
            self.dfs(line + nums[i], nums[:i] + nums[i+1:], k)

if __name__  == "__main__":
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(4, 14))  #TLE case sol 2
    print(Solution().getPermutation(8, 38790))  #TLE case sol 2
    for x in xrange(1, 16): 
        print(Solution2().getPermutation(4, x))
