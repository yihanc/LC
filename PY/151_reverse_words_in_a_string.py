# 151. Reverse Words in a String My Submissions QuestionEditorial Solution
# Total Accepted: 101685 Total Submissions: 647614 Difficulty: Medium
# Given an input string, reverse the string word by word.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# 
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
# 
# click to show clarification.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(list(reversed(s.split())))
