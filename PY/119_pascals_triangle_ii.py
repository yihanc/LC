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
