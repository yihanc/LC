# 207. Course Schedule Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 72501
# Total Submissions: 234449
# Difficulty: Medium
# Contributors: Admin
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# 
# For example:
# 
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
# 
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
# 
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

# 2018.03.22
# Topological Sort
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ins = [ 0 for i in xrange(numCourses)]
        outs = [ set() for i in xrange(numCourses)]
        
        for cur, pre in prerequisites:
            ins[cur] += 1
            outs[pre].add(cur)
            
        d = deque()
        res = []
        for i in xrange(len(ins)):
            if ins[i] == 0: 
                d.appendleft(i)
                
        while d:
            node = d.pop()
            res.append(node)
            for neighbor in outs[node]:
                ins[neighbor] -= 1
                if ins[neighbor] == 0: d.appendleft(neighbor)
        return len(res) == numCourses
            
                

# 2017.03.14
# Algorithm Wiki Topological Sort 
# 1. Traverse and update indegrees[]
# 2. For indegrees = 0, add into deque
# 3. For node in deque. Do BFS and update count. Add node only 

from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[] for _ in xrange(numCourses)]
        indegree = [0] * numCourses
        
        for i in xrange(len(prerequisites)):
            cur, pre = prerequisites[i]
            matrix[pre].append(cur)
            indegree[cur] += 1
        
        count = 0
        d = deque()
        for i in xrange(numCourses):
            if indegree[i] == 0:
                d.appendleft(i)
        
        while d:
            cur = d.pop()
            count += 1
            neighbors = matrix[cur]
            for n in neighbors:
                indegree[n] -= 1
                if indegree[n] == 0:
                    d.appendleft(n)
                    
        return count == numCourses
        

if __name__ == "__main__":
    # n = 5
    # pres = [[0,1], [1,2], [2,0], [3,0], [0, 4]]
    n = 12 
    pres = [[11, 5], [11, 7], [8, 7], [8, 3], [2, 11], [9, 11], [10, 11], [9, 8], [10, 3]]
    print(pres)
    Solution().canFinish(n, pres)
