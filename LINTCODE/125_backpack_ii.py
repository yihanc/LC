# 125. Backpack II 
# Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?
# 
#  Notice
# You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.
# 
# Have you met this question in a real interview? Yes
# Example
# Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.
# 
# 

# 12.30.2017
class Solution:
    """
    @param: m: An integer m denotes the size of a backpack
    @param: A: Given n items with size A[i]
    @param: V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        m, n = len(A), m
        
        dp = [ [ (False, 0) for j in xrange(n + 1) ] for i in xrange(m + 1) ]
        
        dp[0][0] = (True, 0)
        res = 0
        
        for i in xrange(1, m + 1):
            for j in xrange(n + 1):
                dp[i][j] = dp[i-1][j]
                if j >= A[i-1] and dp[i-1][j - A[i-1]][0]:
                    dp[i][j] = (True, max(dp[i][j][1], dp[i-1][j - A[i-1]][1] + V[i-1]))
                    res = max(res, dp[i][j][1])
        return res
        
                    
        
        
m = 300
A = [95,75,23,73,50,22,6,57,89,98]
V = [89,59,19,43,100,72,44,16,7,64]

Solution().backPackII(m, A, V)
