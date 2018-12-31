# 301. Remove Invalid Parentheses Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 35227
# Total Submissions: 101043
# Difficulty: Hard
# Contributors: Admin
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and ).
# 
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]

# TLE Case: "()())())))())(()"
# MLE Case: ")k)))())()())))())"
# Wrong case: "())(((()m)("

# 2018.12.31
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.reverse(res, s, 0, 0, ["(", ")"])
        return res

    def reverse(self, res, s, last_i, last_j, par):
        count = 0
        for i in xrange(last_i, len(s)):
            if s[i] == par[0]: count += 1
            if s[i] == par[1]: count -= 1
            if count >= 0: continue
            
            for j in xrange(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                    self.reverse(res, s[:j] + s[j+1:], i, j, par)
            return
    
        s = s[::-1]
        if par[0] == "(":
            self.reverse(res, s, 0, 0, [par[1], par[0]])
        else:
            res.append(s)
    

# 2017.0318 DFS + Reverse, Fast but tricky algorithm
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, s, 0, 0, ["(", ")"])
        return res
    
    def dfs(self, res, s, lasti, lastj, pair):
        lp = 0
        for i in xrange(lasti, len(s)):
            if s[i] == pair[0]:
                lp += 1
            elif s[i] == pair[1]:
                lp -= 1
                
            if lp >= 0: continue
        
            for j in xrange(lastj, i + 1):
                if s[j] == pair[1] and (j == 0 or s[j-1] != s[j]):
                    self.dfs(res, s[:j] + s[j+1:], i, j, pair)  # string len n - 1, pass i, j to next level
            return      # return here. Only checking reverse when lasti == len(s), means s finished
        
        if pair[0] == "(":
            self.dfs(res, s[::-1], 0, 0, [")", "("])
        else:
            res.append(s[::-1])
        
        


# 2017.0318 BFS slow
# visited set([]) + deque()

from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = set([])
        res = []
        d = deque()
        ansFound = False
        
        d.append(s)
        while d:
            cur = d.pop()
            
            if self.isValid(cur):
                res.append(cur)
                ansFound = True
            
            if ansFound: continue
        
            for i in xrange(len(cur)):
                if cur[i] not in "()":
                    continue
                
                nex = cur[:i] + cur[i+1:]
                
                if nex not in visited: 
                    d.appendleft(nex)
                    visited.add(nex)
                
        return res
        
    def isValid(self, s):
        lp = 0
        
        for i in xrange(len(s)):
            if s[i] not in "()":
                continue
            
            if s[i] == ")":
                if lp <= 0:
                    return False
                else:
                    lp -= 1
            
            if s[i] == "(":
                lp += 1
        
        return lp == 0
