# 344. Reverse String   My Submissions QuestionEditorial Solution
# Total Accepted: 18485 Total Submissions: 31451 Difficulty: Easy
# Write a function that takes a string as input and returns the string reversed.
# 
# Example:
# Given s = "hello", return "olleh".
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        S = list(s)
        i, j = 0, len(S)-1
        while i < j:
            S[i], S[j] = S[j], S[i]
            i, j = i+1, j-1
        
        return ''.join(S)
