# 87. Scramble String  QuestionEditorial Solution  My Submissions
# Total Accepted: 53331
# Total Submissions: 192543
# Difficulty: Hard
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
# 
# Below is one possible representation of s1 = "great":
# 
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
# 
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
# 
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# 
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
# 
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
# 
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
#        print(s1 + " " + s2)
        m, n = len(s1), len(s2)

        if s1 == s2:
            return True
        
        if m != n:
            return False
        
        s = [ 0 for x in xrange(256) ]
        
        for i in xrange(m):
            s[ord(s1[i])] += 1
            s[ord(s2[i])] -= 1
#        print(s)
        
        for i in xrange(256):
            if s[i] != 0:
                return False
                
        for i in xrange(1, m):      # Watch out the divide. g reat, gr eat, gre at, grea, t
            if (( self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) ) or
                (self.isScramble(s1[:i], s2[m-i:]) and self.isScramble(s1[i:], s2[:m-i]) )):
                return True

        return False

if __name__ == "__main__":
    print Solution().isScramble("great", "rgtae")
