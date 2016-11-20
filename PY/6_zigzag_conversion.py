# 6. ZigZag Conversion My Submissions QuestionEditorial Solution
# Total Accepted: 88479 Total Submissions: 367012 Difficulty: Easy
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# Subscribe to see which companies asked this question

# 11.18.2016
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        
        A = [ "" for x in xrange(numRows)]
        res = ""
        
        i = 0
        while i < len(s):
            row = i % (2 * (numRows - 1))
            if row >= numRows:
                row = 2 * (numRows - 1) - row
            
            A[row] += s[i]
            i += 1
        
        return "".join(A)
           
        

class Solution2(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 2 or numRows == 1:
            return s
            
        #1 Generate res[]
        tmp = ["" for x in xrange(numRows)]
        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                tmp[j] += s[i]
                i, j = i + 1, j + 1
            j -= 2
            while j > 0 and i < len(s):
                tmp[j] += s[i]
                i, j = i + 1, j - 1
        
        #2 Generate str from res[]
        res = ""
        for i in tmp:
            res += i
        return res
