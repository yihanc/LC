# 174. Dungeon Game  QuestionEditorial Solution  My Submissions
# Total Accepted: 29666
# Total Submissions: 133649
# Difficulty: Hard
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
# 
# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
# 
# In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
# 
# 
# Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
# 
# For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
# 
# -2 (K)  -3  3
# -5  -10 1
# 10  30  -5 (P)
# 
# Notes:
# 
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        res = [[False ] * n] * m
        
        if dungeon[0][0] >= 0:
            res[0][0] = 1
        else:
            res[0][0] = abs(dungeon[0][0]) + 1

        i = 1
        while i < m:
            res[i][0] = dungeon[i][0] + res[i-1][0]
            if res[i][0] >= 0:
                res[i][0] = 1
            else:
                res[i][0] = abs(res[i][0]) + 1
            i += 1

        j = 1
        while j < n:
            res[0][j] = dungeon[0][j] + res[0][j-1]
            if res[0][j] >= 0:
                res[0][j] = 1
            else:
                res[0][j] = abs(res[0][j]) + 1
            j += 1
        
        i, j = 1, 1
        while i < m:
            while j < n:
                res[i][j] = dungeon[i][j] + min(res[i-1][j], res[i][j-1])
                if res[i][j] >= 0:
                    res[i][j] = 1
                else:
                    res[i][j] = abs(res[i][j]) + 1
                j += 1
            i += 1
        
        return res[m-1][n-1]

if __name__ == "__main__":
    print(Solution().calculateMinimumHP([[0, 0]]))
    print(Solution().calculateMinimumHP([[100]]))
    print(Solution().calculateMinimumHP([[-200]]))
    print(Solution().calculateMinimumHP([[0, -3]]))
