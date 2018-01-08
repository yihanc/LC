class Solution:
    
    """
    @param: nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        def _dfs(line, nums):
            res.append(line)
            
            for i, num in enumerate(nums):
                _dfs(line + [num], nums[i+1:])
        
        nums.sort()
        res = []
        _dfs([], nums)
        return res
