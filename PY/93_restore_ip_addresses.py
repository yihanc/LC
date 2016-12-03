# 93. Restore IP Addresses   QuestionEditorial Solution  My Submissions
# Total Accepted: 69932
# Total Submissions: 275912
# Difficulty: Medium
# Contributors: Admin
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# 11.30.2016 Rewrite
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if len(s) > 12: return []
        self.dfs(res, [], s, 0)
        return res
    
    def dfs(self, res, line, s, start):
        if len(line) == 4 and start == len(s):
            res.append(".".join(line))
            return
     
        if start >= len(s):
            return
        
        for l in xrange(1, 4):
            cur = s[start:start+l]
            if (( l == 1 ) 
                or ( l == 2 and int(cur) >= 10 and int(cur) <= 99)
                or ( l == 3 and int(cur) >= 100 and int(cur) <= 255)):
                self.dfs(res, line + [cur], s, start+l)


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, line, res):
        n = len(line)
        if n > 4 or (not s and n < 4):
            return
        
        if not s and n == 4:
            tmp = ".".join(line)
            res.append(tmp)
            return
        
        i = 0
        while i < 3 and i < len(s):
            num = s[:i+1]
            if num[0] == "0" and i > 0:     # Exclude "0X", "0XX" case
                i += 1
                continue
            if int(num) >= 0 and int(num) <= 255:
                self.dfs(s[i+1:], line + [num], res)
            i += 1

