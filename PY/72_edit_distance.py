# 72. Edit Distance  QuestionEditorial Solution  My Submissions
# Total Accepted: 68726
# Total Submissions: 229657
# Difficulty: Hard
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
# 
# You have the following 3 operations permitted on a word:
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character
# Subscribe to see which companies asked this question

# 11.27.2016 Rewrite
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
        
        for j in xrange(n+1):
            dp[0][j] = j
        
        for i in xrange(1, m+1):
            dp[i][0] = i
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + 1)
        
        return dp[-1][-1]

class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        dp = [[ 0 for j in xrange(n+1)] for i in xrange(m+1)]
        
        for j in xrange(1, n+1):
            dp[0][j] = j
        
        for i in xrange(1, m+1):
            dp[i][0] = i
            
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]) + 1)
                else:
                    dp[i][j] = min(dp[i-1][j-1] + 1 , min(dp[i-1][j], dp[i][j-1]) + 1)

        for i in xrange(len(dp)):
            print(dp[i])
        return dp[-1][-1]
                    
if __name__ == "__main__":
    Solution().minDistance("aaa", "abba")
