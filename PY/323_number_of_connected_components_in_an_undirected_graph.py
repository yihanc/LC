# 323. Number of Connected Components in an Undirected Graph Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 24204 Total Submissions: 50817 Difficulty: Medium Contributor: LeetCode
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
# 
# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
# 
# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# 
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


# 2017.05.26
# Union find. Count diff
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        roots = [ x for x in xrange(n)]
        for e in edges:
            x = self.find(roots, e[0])
            y = self.find(roots, e[1])
            if x != y:
                roots[x] = y
                n -= 1
        return n
    
    def find(self, roots, id):
        while roots[id] != id:
            roots[id] = roots[roots[id]]
            id = roots[id]
        return id
