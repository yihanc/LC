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

# 2018.06.12 Rewrite using a helper functions.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = "1"
        while n > 1:
            tmp = self.gen_next_lvl(tmp)
            n -= 1
        return tmp
    
    def gen_next_lvl(self, s):
        res = ""
        count = 1
        i = 0
        while i < len(s):
            if i == len(s) - 1 or s[i] != s[i+1]:                   # When do we need to stop and output?
                res += str(count) + s[i]                            # 1) i is at the end
                                                                    # 2) cur char is different than the last char
                
                count = 1                                           # Reset count to 1
            else:                                                   # Else, cur char == next char
                count += 1
            i += 1  
        return res
                

# 2017.03.11. Rewrite
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0: return ""
        res = "1"
        
        while n > 1:
            tmp = res
            res = ""
            
            for i in xrange(len(tmp)):
                if i == 0 or tmp[i] != tmp[i - 1]:
                    char = tmp[i]
                    count = 1
                else:
                    count += 1
                    
                if i == len(tmp) - 1 or (i + 1 < len(tmp) and tmp[i] != tmp[i+1]):
                    res += str(count) + char

            n -= 1
        return res
        

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
