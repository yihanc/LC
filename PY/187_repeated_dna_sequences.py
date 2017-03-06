# 187. Repeated DNA Sequences Add to List
# Description  Submission  Solutions
# Total Accepted: 67869
# Total Submissions: 225662
# Difficulty: Medium
# Contributors: Admin
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# 
# For example,
# 
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# 
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
# Subscribe to see which companies asked this question.


# 2017.02.25
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        n = len(s)
        res = set([])
        for i in xrange(n):
            tmp = s[i:i+10]
            dic[tmp] = dic.get(tmp, 0) + 1
            if dic[tmp] > 1:
                res.add(tmp)
        return list(res)
        
