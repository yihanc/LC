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
        if len(s) <= 1:
            return s
    
        l = list(s)
    
        for i,char in enumerate(l):
            if i >= len(l) / 2:
                return ''.join(l)
            tmpchar = l[-(i+1)]
            l[-(i+1)] = l[i]
            l[i] = tmpchar
    
        return ''.join(l)
