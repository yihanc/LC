# 399. Evaluate Division Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 14161
# Total Submissions: 35014
# Difficulty: Medium
# Contributor: LeetCode
# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
# 
# According to the example above:
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
# 
# Subscribe to see which companies asked this question.

# 2017.05.11 Rewite 
# Floyd-warshall graph algorithms
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        quot = collections.defaultdict(dict)
        for i in xrange(len(equations)):
            x, y = equations[i]
            quot[x][x] = quot[y][y] = 1.0
            quot[x][y] = values[i]
            quot[y][x] = 1 / values[i]
        for k in quot:              # for k, i, j in itertools.permutations(quot, 3)
            for i in quot[k]:
                for j in quot[k]:
                    quot[i][j] = quot[i][k] * quot[k][j]
        res = []
        #print(quot)
        for x, y in queries:
            if x not in quot or y not in quot[x]:
                res.append(-1.0)
            else:
                res.append(quot[x][y])
        return res
