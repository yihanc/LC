class Solution:
    """
    @param: n: Given the range of numbers
    @param: k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        def _dfs(line, nums):
            if len(line) == k:
                res.append(line)
                return
            
            for i, num in enumerate(nums):
                _dfs(line + [num], nums[i+1:])
            
        res = []
        _dfs([], [x for x in xrange(1, n + 1)])
        return res
