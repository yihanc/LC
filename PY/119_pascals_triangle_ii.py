# 119. Pascal's Triangle II  QuestionEditorial Solution  My Submissions
# Total Accepted: 91292
# Total Submissions: 267357
# Difficulty: Easy
# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
# 
# Subscribe to see which companies asked this question

# 12.3.2016 Rewrite
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        
        i = 0
        while i <= rowIndex:
            res.append(1)
            for x in xrange(len(res) - 2, 0, -1):
                res[x] += res[x-1]
            i += 1
            
        return res

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        
        i = rowIndex
        while i > 0:
            j = len(res) - 1
            while j > 0:
                res[j] = res[j] + res[j-1]
                j -= 1

            res = res + [1]
            i -= 1
            
        return res
