# 97. Interleaving String  QuestionEditorial Solution  My Submissions
# Total Accepted: 57793
# Total Submissions: 246014
# Difficulty: Hard
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
# 
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
# 
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        return self.dfs(s1, s2, s3, 0, 0)

    def dfs(self, s1, s2, s3, i, j):
        if i == len(s1) and j == len(s2):
            return True
        
        res1, res2 = False, False
        if i < len(s1) and i + j < len(s3) and s1[i] == s3[i+j]:
            res1 = self.dfs(s1, s2, s3, i+1, j)

        if j < len(s2) and i + j < len(s3) and s2[j] == s3[i+j]:
            res2 = self.dfs(s1, s2, s3, i, j+1)

        if res1 or res2:
            return True
        else:
            return False
        

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    #s3 = "aadbbcbcac"
    s3 = "aadbbbaccc"
    print(Solution().isInterleave(s1, s2, s3))
