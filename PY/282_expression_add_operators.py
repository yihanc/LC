# 282. Expression Add Operators Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 26850
# Total Submissions: 92446
# Difficulty: Hard
# Contributors: Admin
# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
# 
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []

# 2017.03.16 DFS 

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []
        res = []
        self.dfs(res, "", num, target, 0, 0, 0)
        return res
    
    def dfs(self, res, line, num, target, start, last, multi):
        #print(line, last, multi, start)
        if start == len(num) and last == target:
            res.append(line)
            return

        for i in xrange(start, len(num)):
            cur = num[start:i+1]
            
            if not line:
                self.dfs(res, cur, num, target, i + 1, int(cur), 0)
            else:
                self.dfs(res, line + "+" + cur, num, target, i + 1, last + int(cur), last)
                self.dfs(res, line + "-" + cur, num, target, i + 1, last - int(cur), last)
                self.dfs(res, line + "*" + cur, num, target, i + 1, (last - multi) * int(cur) + multi, multi)
            
            if num[start] == "0":   # Handle number start with "0"
                return
                
