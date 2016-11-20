# 38. Count and Say My Submissions QuestionEditorial Solution
# Total Accepted: 83436 Total Submissions: 283284 Difficulty: Easy
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
# 
# Note: The sequence of integers will be represented as a string.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""

        res = "1"

        while n > 1:
            tmp, res, count, curChar = res, "", 0, ""
            for i, char in enumerate(tmp):
                if i == 0 or char != tmp[i-1]:
                    if count >= 1:
                        res = res + str(count) + cur_char
                    cur_char = char
                    count = 1
                else:
                    count += 1
            res = res + str(count) + cur_char
            n -= 1
            
        return res
