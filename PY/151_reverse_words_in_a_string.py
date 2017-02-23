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
        res = s.split()
        i, j = 0, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i, j = i + 1, j - 1
        return " ".join(res)


if __name__ == "__main__":
    s = "    the sky is blue"
    print(Solution().reverseWords(s))
