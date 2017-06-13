# 139. Word Break  QuestionEditorial Solution  My Submissions
# Total Accepted: 107437
# Total Submissions: 396355
# Difficulty: Medium
# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
#  = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s) 
        dp = [ False for x in xrange(n + 1) ]
        dp[0] = True
        for i in xrange(n):
            for j in xrange(i+1, n+1):
                cur = s[i:j]
                if cur in wordDict and dp[i]:
                    dp[j] = True
        print(dp)
        return dp[-1]
                

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))
            
