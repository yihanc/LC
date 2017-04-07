# 310. Minimum Height Trees Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 29724
# Total Submissions: 103771
# Difficulty: Medium
# Contributor: LeetCode
# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.
# 
# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).
# 
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
# 
# Example 1:
# 
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
# 
#         0
#         |
#         1
#        / \
#       2   3
# return [1]
# 
# Example 2:
# 
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
# 
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]
# 
# Hint:
# 
# How many MHTs can a graph have at most?
# Note:
# 
# (1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
# 
# (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
# 
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.

# 2017.04.05 Similar to Topological sort. From leafs to center till n <= 2
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        udg = [ set() for _ in xrange(n) ]
        for n1, n2 in edges:
            udg[n1].add(n2)
            udg[n2].add(n1)
        
        leaves = [ x for x in xrange(n) if len(udg[x]) == 1 ]
        
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                j = udg[i].pop()
                udg[j].remove(i)
                if len(udg[j]) == 1: newleaves.append(j)
            leaves = newleaves
        return leaves


# 2017.04.05 TLE for large cases
# 1. For each node create dic for neighbors
# 2. Go through the node and push to a minheap if h <= hq[0][0]
# 3. Pop and create result

from collections import defaultdict, deque
from heapq import *
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        for n1, n2 in edges:
            dic[n1].append(n2)
            dic[n2].append(n1)
        print(dic)
        res = []
        hq = []
        for i in xrange(n):
            vis = [ False for x in xrange(n) ]
            d = deque()
            d.append([1, i])
            vis[i] = True
            while d:
                h, node = d.pop()
                if hq and h > hq[0][0]: break
                for nextlvl in dic[node]:
                    if vis[nextlvl]: continue
                    d.appendleft([h + 1, nextlvl])
                    vis[nextlvl] = True
            if not hq or h <= hq[-1][0]:
                heappush(hq, [h, i])
        
        print("hq", hq)
        if not hq: return []
        minh = hq[0][0]
        while hq:
            res.append(heappop(hq)[1])
            if not hq or hq[0][0] != minh: 
                return res
        
        
                
