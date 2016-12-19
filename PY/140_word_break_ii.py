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

# 12.08.2016 Rewrite. DP + DFS
class Solution(object):
    dp = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)
        self.dp = [ False for x in xrange(len(s)+1) ]
        self.dp[0] = True
        
        for i in xrange(n):
            for j in xrange(i+1):
                tmp = s[j:i+1]
                if tmp in wordDict and self.dp[j]:
                    self.dp[i+1] = True
                    break
        
        if not self.dp[-1]: return []
        res = []
        self.dfs(res, "", s, n-1, wordDict)
        return res
    
    def dfs(self, res, line, s, end, wordDict):
        if end == -1:
            res.append(line[:-1])
            return
        
        for start in xrange(end, -1, -1):
            tmp = s[start:end+1]
            if tmp in wordDict and self.dp[start]:
                self.dfs(res, tmp + " " + line, s, start - 1, wordDict)

# DP + DFS can get rid of TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        n = len(s)
        print(s)
        print(wordDict)
        res = []

        dp = [False for x in xrange(n+1)]
        dp[n] = True
        for i in xrange(n-1, -1, -1):
            for j in xrange(n-1, i-1, -1):      # Better loop. i start index. j end index
                if dp[j+1] and s[i:j+1] in wordDict:
                    dp[i] = True
                    break

#        for i in xrange(n-1, -1, -1):
#            for j in xrange(i, -1, -1):
#                if dp[i+1] and s[j:i+1] in wordDict:
#                    dp[j] = True
#                    continue
        
        def dfs(start, line):
            if not dp[start]:
                return
            
            if start == len(s):
                res.append(line[1:])
                return
    
            for i in xrange(start, len(s)):
                if dp[i+1] and s[start:i+1] in wordDict:
                    dfs(i+1, line + " " + s[start:i+1])   

        dfs(0, "")
        return res
        
if __name__  == "__main__":
#    s = "catsanddog"
#    d = ["cat","cats","and","sand","dog"]
#    Solution().wordBreak(s, d)
#    s = "goalspecial"
#    d = ["go","goal","goals","special"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    d = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(s, d))
#    Solution().wordBreak(s, d)
#    s1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#    d1 = ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]
#    Solution().wordBreak(s1, d1)

exit

# If DFS only. get TLE 
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []

        # Precheck to get rid of TLE
        set_s = set(s)
        set_dict = set("".join(wordDict))
        for char in set_s:
            if set_s not in set_dict:
                return []

        self.dfs(s, wordDict, res, "")
        return res
        
    def dfs(self, s, wordDict, res, line):
        if not s:
            print(line)
            res.append(line)
            return
        
        for i in xrange(1, len(s)+1):
            if s[:i] in wordDict:
                if not line:
                    self.dfs(s[i:], wordDict, res, s[:i])
                else:
                    self.dfs(s[i:], wordDict, res, line + " " + s[:i])
