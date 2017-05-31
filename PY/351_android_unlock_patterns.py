# 351. Android Unlock Patterns Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 12618
# Total Submissions: 29166
# Difficulty: Medium
# Contributor: LeetCode
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
# 
# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.
# 
# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6 
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
# 
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
# 
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
# 
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
# 
# Example:
# Given m = 1, n = 1, return 9.
# 
# Credits:
# Special thanks to @elmirap for adding this problem and creating all test cases.


# 2017.05.27
# DFS + skip dic
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = [ [ -1 for y in xrange(9)] for x in xrange(9) ]
        skip[0][2] = skip[2][0] = 1
        skip[6][8] = skip[8][6] = 7
        skip[0][6] = skip[6][0] = 3
        skip[2][8] = skip[8][2] = 5
        skip[0][8] = skip[8][0] = skip[2][6] = skip[6][2] = skip[1][7] = skip[7][1] = skip[3][5] = skip[5][3] = 4

        res = [0, 0, 0]
        self.dfs(res, [0], skip, m, n)
        self.dfs(res, [1], skip, m, n)
        self.dfs(res, [4], skip, m, n)
        return res[0] * 4 + res[1] * 4 + res[2]
    
    def dfs(self, res, line, skip, m, n):
        if len(line) >= m and len(line) <= n:
            if line[0] == 0: res[0] += 1
            if line[0] == 1: res[1] += 1
            if line[0] == 4: res[2] += 1

        if len(line) == n: return
        
        for i in xrange(9):
            if i in line: continue
            if skip[line[-1]][i] != -1 and skip[line[-1]][i] not in line: continue
            self.dfs(res, line + [i], skip, m, n)

