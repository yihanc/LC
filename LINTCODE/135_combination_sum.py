class Solution:
    """
    @param: candidates: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        def _dfs(line, nums):
            if sum(line) > target: 
                return
            
            if sum(line) == target:
                res.append(line)
                return
        
            for i, num in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                
                _dfs(line + [num], nums[i:])
        
        candidates.sort()    
        res = []
        _dfs([], candidates)
        return res

