# 5. Longest Palindromic Substring   My Submissions QuestionEditorial Solution
# Total Accepted: 108992 Total Submissions: 469979 Difficulty: Medium
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #1 Preprocess Manacher's Algorithm
        new_s = "^#" + "#".join(list(s)) + "#$"

        #2 Get P[]
        center, right = 0, 0
        P = [0 for x in range(len(new_s))

        i = 1
        while i < len(new_s):
            i_mirror = 2 * center - i
            P[i] = min(right - i, P[i_mirror]) if right > i else 0
            while new_s[i + P[i] + 1] == new_s[i - P[i] -1]: 
                P[i] += 1
            if i + P[i] > right:
                right = i + P[i]
                center = i
            i += 1

        #3 Get result
        mx = max(P)
        center = P.index(mx)
        return new_s[center-mx : center+mx+1].replace("#", "")
