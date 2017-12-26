class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        max_reach = 0
        i = 0 
        while i <= max_reach:
            max_reach = max(max_reach, A[i] + i)
            if max_reach >= len(A) - 1: return True
            i += 1
        return False
            
