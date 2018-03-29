# 210. Course Schedule II Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 54067
# Total Submissions: 205100
# Difficulty: Medium
# Contributors: Admin
# There are a total of n courses you have to take, labeled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
# 
# For example:
# 
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
# 
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
# 
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites

# 2018.03.22 Topological sort`
from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ins = [ 0 for i in xrange(numCourses)]
        outs = [ set() for i in xrange(numCourses)]
        
        for cur, pre in prerequisites:
            ins[cur] += 1
            outs[pre].add(cur)
        
        d = deque()
        for i in xrange(len(ins)):
            if ins[i] == 0: d.appendleft(i)
        
        res = []
        while d:
            node = d.pop()
            res.append(node)
            for neighbor in outs[node]:
                ins[neighbor] -= 1
                if ins[neighbor] == 0: d.appendleft(neighbor)
        
        return res if len(res) == numCourses else []

# 2017.03.25 Rewrite
from collections import *
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        inlines = [ 0 for x in xrange(n) ]
        outlines = defaultdict(list)
        d = deque()
        res = []
        count = 0
        
        for cur, pre in prerequisites:
            inlines[cur] += 1
            outlines[pre].append(cur)
        
        for i in xrange(len(inlines)):
            if inlines[i] == 0: d.append(i)
        
        while d:
            cur = d.pop()
            count += 1
            res.append(cur)
            for nextlvl in outlines[cur]:
                inlines[nextlvl] -= 1
                if inlines[nextlvl] == 0:
                    d.appendleft(nextlvl)
        return res if count == n else [] 
            
        

from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        matrix = [ [] for _ in xrange(numCourses) ]
        indegree = [ 0 for _ in xrange(numCourses) ]
        
        for i in xrange(len(prerequisites)):
            cur, pre = prerequisites[i]
            matrix[pre].append(cur)
            indegree[cur] += 1
        
        d = deque()
        for i in xrange(numCourses):
            if indegree[i] == 0:
                d.appendleft(i)
                
        while d:
            cur = d.pop()
            res.append(cur)
            for neighbor in matrix[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    d.appendleft(neighbor)
        
        return res if len(res) == numCourses else []
        
        


