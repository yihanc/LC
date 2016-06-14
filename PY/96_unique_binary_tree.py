# 96. Unique Binary Search Trees My Submissions QuestionEditorial Solution
# Total Accepted: 84526 Total Submissions: 224165 Difficulty: Medium
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#      4        4     4       4     4
#     /        /     /       /     /
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#    1         3      3       2      1          2
#     \       / \    / \     / \      \        / \
#      3     2   4  1  4    1   3      2      1   4
#     / \    /       \           \      \         /
#    2   4  1         2           4      3       3
#                                         \
#                                          4
#
# Subscribe to see which companies asked this question
# Analysis:
# n = 0, 1
# n = 1, 1
# n = 2, 2 = (0,1) + (1,0)
# n = 3, 5 = 2(0,2) + 2(2,0) + 1(1,1)
# n = 4, 10 = (0,3), (1,2), (2,1), (0,3)
# n = 5,  

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0

        res = [0 for x in xrange(0,n+1)]
        res[0], res[1] = 1, 1

        for n in xrange(2, n+1):
            i, tmp = 0, 0 
            while i < n:
                tmp += res[i] * res[n-1-i]
                i += 1
            res[n] = tmp

        return res[n]

import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        self.assertEqual(Solution().numTrees(3), 5)

    def test_1(self):
        self.assertEqual(Solution().numTrees(2), 2)

    def test_2(self):
        self.assertEqual(Solution().numTrees(4), 14)

if __name__ == "__main__":
    unittest.main()
