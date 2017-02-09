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

# 12.30.2016 Rewrite
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False
        if not s1 and not s2: return True
        if not s1 or not s2: return False
        if s1 == s2: return True
        dic = {}
        for char in s1:
            dic[char] = dic.get(char, 0) + 1
        
        for char in s2:
            if char not in dic: return False
            dic[char] -= 1
        
        for key in dic:
            if dic[key] != 0:
                return Falsek
        
        n = len(s1)
        for i in xrange(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
        
        return False
            

if __name__ == "__main__":
    # s1, s2 = "great", "rgtae"
    # s1, s2 = "abcdefghijklmn", "efghijklmncadb"
    s1, s2 = "abcd", "cadb"
    print(s1, s2)
    print(Solution().isScramble(s1, s2))
