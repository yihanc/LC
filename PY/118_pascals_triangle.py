# 118. Pascal's Triangle  QuestionEditorial Solution  My Submissions
# Total Accepted: 102669
# Total Submissions: 288171
# Difficulty: Easy
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

# 12.3.2016 Rewrite
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows <= 0: return res
        
        i = 0
        while i < numRows:
            res.append([1] * (i+1))
            i += 1
        
        for i in xrange(2, numRows):
            for j in xrange(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
                
        return res


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        for i in xrange(numRows):
            res.append([1])
            for j in xrange(1, i+1):
                if j == i:
                    res[i].append(res[i-1][j-1])
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
        
        return res
                

if __name__ == "__main__":
    print(Solution().generate(5))
