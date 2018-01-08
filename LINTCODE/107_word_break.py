from collections import defaultdict
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        dp = [ False for i in xrange(n + 1) ]
        
        # Pre check to pass large case
        dict_map = defaultdict(int)
        for word in dict:
            for char in word:
                dict_map[char] += 1
        
        for char in s:
            if char not in dict_map: return False
            
        dp[0] = True
        
        for end in xrange(1, n + 1):
            for start in xrange(end - 1, -1, -1):   # Go reverse way to pass test case 21..
                #print(s[start:end], dp[start])
                if s[start:end] in dict and dp[start]:
                    dp[end] = True
                    if dp[-1]: return True
                    break
        #print(dp)
        return dp[-1]
