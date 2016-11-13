# 68. Text Justification   QuestionEditorial Solution  My Submissions
# Total Accepted: 43804
# Total Submissions: 248285
# Difficulty: Hard
# Contributors: Admin
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is inserted between words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.
# 
# click to show corner cases.
# 
# Corner Cases:
# A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
# Subscribe to see which companies asked this question

# Algorithms:
# 1. Get words in list to form the line.
# 2. For padding 0, pad 0 except for last word.
# 3. Add remaining to the last line if needed.

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, line = [], []
        cur_len = 0
        
        for word in words:
            if cur_len + len(word) > maxWidth: 
                res.append(self.generateLine(line, maxWidth))
                cur_len = len(word) + 1
                line = [word]
                continue
            
            cur_len += len(word) + 1
            line.append(word)
        
        if line:
            last_line = " ".join(line)
            last_line += " " * (maxWidth - len(last_line))
            res.append(last_line)
        return res

    
    def generateLine(self, line, maxWidth):
        if len(line) == 1:              # Corner case. one word in line
            return line[0] + " " * (maxWidth - len(line[0]))
            
        for word in line:
            maxWidth -= len(word)
        
        i = 0
        while i < len(line) - 1 and maxWidth > 0:       # Note i < len(line) - 1. Distributing 0 except for last word
            line[i] += " "
            maxWidth, i = maxWidth - 1, i + 1
            if i == len(line) - 1:          # Repeat the loop
                i = 0
        
        return "".join(line)

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text"]# , "justification."]
#    words = [""]
    for row in Solution().fullJustify(words, 16):
        print([row])
