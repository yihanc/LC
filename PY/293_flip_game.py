# 293. Flip Game Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 22862
# Total Submissions: 41548
# Difficulty: Easy
# Contributor: LeetCode
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
# 
# Write a function to compute all possible states of the string after one valid move.
# 
# For example, given s = "++++", after one move, it may become one of the following states:
# 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].

# 2017.05.20
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        if n <= 1: return []
        res = []
        for i in xrange(1, n):
            tmp = s[i-1:i+1]
            if tmp == "++":
                res.append(s[:i-1] + "--" + s[i+1:])
        return res