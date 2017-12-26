class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        res = 0
        for num in A:
            res ^= num
        return res
            
