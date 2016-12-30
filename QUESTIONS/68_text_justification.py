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
# 1. words[i j] for the line to be inserted
# 2. Pad space for the line. 

# 12.10.2016 Rewrite
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: return []
        res = []
        n = len(words)

        i = 0
        while i < n:
            L = 0
            j = i                                         # Find words[i:j+1] for current line
            while j < n:    
                if L == 0 and len(words[j]) <= maxWidth:
                    L += len(words[j])
                elif L != 0 and L + 1 + len(words[j]) <= maxWidth:
                    L += len(words[j]) + 1
                else:
                    break
                j += 1
                  
            line = words[i]                               # Creating line
            if j != n:
                count = 0
                for x in xrange(i+1, j):
                    line += " " + " " * ((maxWidth - L) // (j - i - 1))
                    if ((maxWidth - L) % (j - i - 1) - count) > 0:
                        line += " " + words[x]
                    else:
                        line += words[x]
                    count += 1
                if j - i == 1:
                    line += " " * (maxWidth - len(line))
            else:
                for x in xrange(i+1, j):
                    line += " " + words[x]
                line += " " * (maxWidth - len(line))
            res.append(line)
            i = j
        return res

                


if __name__ == "__main__":
    words, n = ["This", "is", "an", "example", "of", "text", "justification."], 16
#    words, n = ["Listen","to","many,","speak","to","a","few."], 6
#    words = [""]
    for row in Solution().fullJustify(words, n):
        print([row])
