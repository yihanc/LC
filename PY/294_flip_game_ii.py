# 294. Flip Game II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23904
# Total Submissions: 52081
# Difficulty: Medium
# Contributor: LeetCode
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
# 
# Write a function to determine if the starting player can guarantee a win.
# 
# For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# 
# Follow up:
# Derive your algorithm's runtime complexity.

# 2017.05.26
# Recursive + Memorization
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        def dfs(s):
            if s not in memo:
                for i in xrange(len(s)):
                    if s[i:i+2] == "++" and not dfs(s[:i] + "-" + s[i+2:]):
                        memo[s] = True
                        break
                if s not in memo: memo[s] = False
            return memo[s]
        return dfs(s)

# This code can be simplify using any()
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def dfs(s):
            if s not in memo:
                memo[s] = any(s[i:i+2] == "++" and not dfs(s[:i] + '-' + s[i+2:]) for i in xrange(len(s)))
            return memo[s]
        memo = {}
        return dfs(s)

