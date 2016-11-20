# 52. N-Queens II   QuestionEditorial Solution  My Submissions
# Total Accepted: 53077
# Total Submissions: 126364
# Difficulty: Hard
# Contributors: Admin
# Follow up for N-Queens problem.
# 
# Now, instead outputting board configurations, return the total number of distinct solutions.
# 
# Subscribe to see which companies asked this question

# Not the best but accepted
class Solution(object):
    count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dfs(self.count, [], 0, n)
        return self.count

    def dfs(self, count, res, dep, n):
        if dep == n:
            self.count += 1
            return

        for i in xrange(n):
            if self.isValid(res, dep, i):
                line = "." * i + "Q" + "."*(n-i-1)  #Generating line
                self.dfs(self.count, res + [line], dep+1, n)  #Note res + [line] for new object)

    def isValid(self, res, dep, col):
        if not res:
            return True
        n = len(res[0])
        for i in xrange(dep):
            if res[i][col] == "Q":  # Same col
                return False
            if col + dep - i < n and res[i][col+dep-i] == "Q":  # 45 Degree right
                return False
            if col - dep + i >= 0 and res[i][col-dep+i] == "Q": # 45 Degree left
                return False
        return True
