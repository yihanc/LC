# 140. Word Break II  QuestionEditorial Solution  My Submissions
# Total Accepted: 68516
# Total Submissions: 321390
# Difficulty: Hard
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# 
# Return all such possible sentences.
# 
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# 
# A solution is ["cats and dog", "cat sand dog"].
# 
# Subscribe to see which companies asked this question

# Notes:
# Forward DP or Backward DP?
# WB1 is forward DP. DP[i] means s[:i+1] is breakable
# WB2 is backward. DP[i] means s[i:] is breakable
# Since DFS is to check remaining string is 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
            
if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))
