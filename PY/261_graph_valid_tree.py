# 261. Graph Valid Tree Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 34387
# Total Submissions: 92185
# Difficulty: Medium
# Contributor: LeetCode
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# 
# For example:
# 
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.


# 2017.05.26
# Union find 
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nums = [ -1 for _ in xrange(n)]
        
        for i in xrange(len(edges)):
            x = self.find(nums, edges[i][0])    #find the parent
            y = self.find(nums, edges[i][1])
            
            if x == y: return False
            
            nums[x] = y
        return len(edges) == n -1
    
    def find(self, nums, i):
        if nums[i] == -1: return i
        return self.find(nums, nums[i])
