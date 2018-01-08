"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here

        res = []
        inlines = [ 0 ] * len(graph)

        for node in graph:
            for neighbor in node.neighbors:
                inlines[neighbor.label] += 1
        
        count = len(graph)
        d = deque()
        for i, inline in enumerate(inlines):
            if inline == 0:
                d.appendleft(graph[i])
                count -= 1
        
        while d:
            cur = d.pop()
            res.append(cur)
            for neighbor in cur.neighbors:
                inlines[neighbor.label] -= 1
                if inlines[neighbor.label] == 0:
                    d.appendleft(neighbor)
                    count -= 1
        
        if count == 0:
            return res
        else:
            raise Exception("Error")
            
                
            
            
