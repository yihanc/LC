# 133. Clone Graph My Submissions QuestionEditorial Solution
# Total Accepted: 67034 Total Submissions: 269478 Difficulty: Medium
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
# 
# 
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
# 
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
# 
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
# 
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
# 
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
# Subscribe to see which companies asked this question
#
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
# Notes:
# 1. Use collections deque for BFS. Popleft
# 2. Use dic to keep track of node/neighbor and its copy

# 2017.02.22 Rewrite
# Step 1: BFS to create nodes and add to DICTIONARY MAPPING
# Step 2: For each node in DIC, add neighbors

from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        dic = {}
        d = deque()
        d.append(node)
        
        while d:
            cur = d.pop()

            cur_clone = UndirectedGraphNode(cur.label)
            dic[cur] = cur_clone
                
            for neighbor in cur.neighbors:
                if neighbor not in dic:
                    d.appendleft(neighbor)
        
        for key in dic:
            for neighbor in key.neighbors:
                dic[key].neighbors.append(dic[neighbor])
            
        return dic[node]


# 12.07.2016 Rewrite
# Careful that graph can be multiple path to the same destination

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return
        dic, visited, d = {}, {}, deque()
        
        d.append(node)
        dic[node] = UndirectedGraphNode(node.label)

        while d:
            cur = d.pop()
            if cur in visited: continue
            visited[cur] = True

            for neighbor in cur.neighbors:
                if neighbor not in dic:
                    dic[neighbor] = UndirectedGraphNode(neighbor.label)

                dic[cur].neighbors.append(dic[neighbor])
                if neighbor not in visited: d.appendleft(neighbor)

        return dic[node]


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None

        node_copy = UndirectedGraphNode(node.label) 
        dic = {node: node_copy}
        queue = collections.dequeue([node])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                # Node not visited
                if neighbor not in dic:
                    neighbor_copy = UndirectedGraphNode(node.label)
                    dic[node].append(neighbor_copy)
                    dic[neighbor] = neighbor_copy
                    queue.append(neighbor)
                # Node visited
                else:
                    dic[node].neighbors.append(dic[neighbor])

        return node_copy
            
