class Solution:
    """
    @param: n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n == 0 or n == 1: return 1
        if n == 2: return 2
        res = [ 0 ] * (n + 1)
        res[0] = 1
        res[1] = 1
        res[2] = 2
        
        i = 3
        while i <= n:
            tmp = 0
            j = 0
            while j < i:
                tmp += res[j] * res[i-j-1] 
                j += 1
            res[i] = tmp
            i += 1
        return res[n]
