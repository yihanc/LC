# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# 
# 
# Example 1:
# 
# Input: k = 3, n = 7
# 
# Output:
# 
# [[1,2,4]]
# 
# Example 2:
# 
# Input: k = 3, n = 9
# 
# Output:
# 
# [[1,2,6], [1,3,5], [2,3,4]]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

# 2017.03.24 Rewrite
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(line, A, tgt):
            if tgt < 0: return
            if tgt == 0 and len(line) == k:
                res.append(line)
                return
            
            if len(line) < k:
                for i in xrange(len(A)):
                    dfs(line + [A[i]], A[i+1:], tgt - A[i])
            
        nums = [ x for x in xrange(1, 10) ]
        res = []
        dfs([], nums, n)
        return res

#
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = range(1, 10)
        print(nums)
        self.dfsHelper(res, nums, [], n, k)
        print(res)
        return res

    def dfsHelper(self, res, nums, line, n, k):
        sumList = sum(line)
        if sumList > n or len(line) > k:
            return
        elif sumList == n and len(line) == k:
            res.append(line)
            return
        else:
            for i, num in enumerate(nums):
                self.dfsHelper(res, nums[i+1:], line + [num], n, k)

if __name__ == "__main__":
    sol = Solution()
    sol.combinationSum3(3, 7)
