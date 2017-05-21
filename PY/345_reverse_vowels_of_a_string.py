# 345. Reverse Vowels of a String   My Submissions QuestionEditorial Solution
# Total Accepted: 11585 Total Submissions: 32869 Difficulty: Easy
# Write a function that takes a string as input and reverse only the vowels of a string.
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# Example 2:
# Given s = "leetcode", return "leotcede".
# 
# Subscribe to see which companies asked this question


# 2017.05.20
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        sl = list(s)
        while i < j:
            if s[i] not in "aeiouAEIOU":
                i += 1
            elif s[j] not in "aeiouAEIOU":
                j -= 1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i, j = i + 1, j - 1
        return "".join(sl)
