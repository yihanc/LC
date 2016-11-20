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

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        l = list(s)
        j = len(l) - 1
        vowels = [ 'a', 'e', 'i', 'o', 'u' ]
        for i, char in enumerate(l):
            if c in vowels:
                while (j > i):
                    if  


1. Move i forward until it hit a vowel

2. Then move j backward until it hit a vowel

if i == j, program ends
swap if they are different.

