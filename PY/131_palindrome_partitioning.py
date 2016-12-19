# 131. Palindrome Partitioning  QuestionEditorial Solution  My Submissions
# Total Accepted: 77173
# Total Submissions: 260026
# Difficulty: Medium
# Given a string s, partition s such that every substring of the partition is a palindrome.
# 
# Return all possible palindrome partitioning of s.
# 
# For example, given s = "aab",
# Return
# 
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
# Subscribe to see which companies asked this question

# 12.7.2016 Rewrite
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(res, [], s, 0)
        return res

    def dfs(self, res, line, s, start):
        if start == len(s):
            res.append(line)
            return

        for j in xrange(start+1, len(s)+1):
            tmp = s[start:j]
            if j - start == 1 or self.isPalindrome(tmp):
                self.dfs(res, line + [tmp], s, j)

    def isPalindrome(self, s):
        if not s or len(s) == 1: return True

        l, r = 0, len(s) -1
        while l < r:
            if s[l] != s[r]: return False
            l, r = l+1, r-1

        return True

# DFS
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, res, [])
        print(res)
        return res
    
    def dfs(self, s, res, line):
        if not s:
            # print(line)
            res.append(line)
            return
        
        for i in xrange(len(s)):
            # print("----" + str(i) + "----")
            if self.isPalindrome(s[:i+1]):
                # print(s[:i+1])
                self.dfs(s[i+1:], res, line + [s[:i+1]]) #1 [s[s:i+1]] Make a list
        
    def isPalindrome(self, s):
        if not s:
            return False
            
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__  == "__main__":
    Solution().partition("aab")
    # print(Solution().isPalindrome("a"))
    # print(Solution().isPalindrome("aa"))
    # print(Solution().isPalindrome("aab"))
