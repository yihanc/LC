class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle or len(triangle) == 0: return 0
        if len(triangle) == 1: return triangle[0][0]
        n = len(triangle)
        
        dp = [ 0 ] * n
        dp[0] = triangle[0][0]

        for i in xrange(1, n):
            cur = float('inf')
            for j in xrange(i, -1, -1):
                if j == i: dp[j] = dp[j-1] + triangle[i][j]
                elif j == 0: dp[j] += triangle[i][j]
                else: dp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
                
                cur = min(cur, dp[j])
            res = cur
                
        return res
                
