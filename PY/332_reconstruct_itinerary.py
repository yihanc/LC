# 332. Reconstruct Itinerary Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 32385
# Total Submissions: 112814
# Difficulty: Medium
# Contributor: LeetCode
# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
# 
# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


# 2018.03.23
# Greedy + Backward DFS
# Algorithm
# 1. Sort tickets backward and construct routes. City with smaller name will appread last. For examplea, { "JFK": ["D", "C", "C", "B", "A" ] }
# 2. Select the next smallest city to visit and pop, visit(routes[city].pop())
# 3. If stuck, append to res. 
# 4. Reverse res to get result

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def visit(airport):
            while routes[airport]:
                visit(routes[airport].pop())
            res.append(airport)
        
        routes = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            routes[a].append(b)
            
        res = []
        visit("JFK")
        return res[::-1]
        


# 2017.05.13
# Eulerian path From Stefan Pochmann
# First keep going forward until you get stuck. That's a good main path already. Remaining tickets form cycles which are found on the way back and get merged into that main path. By writing down the path backwards when retreating from recursion, merging the cycles into the main path is easy - the end part of the path has already been written, the start part of the path hasn't been written yet, so just write down the cycle now and then keep backwards-writing the path.

# Explained
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 
# ATL: SFO -> JFK
# JFK: SFO -> ATL
# SFO: ATL
# 
# visit('JFK'), pop(ATL) + JFK
#    ->  visit('ATL') pop(JFK)  + ATL
#      ->  visit('JFK') pop(SFO)  + JFK
#        -> visit('SFO') pop(ATL)  + SFO
#          -> visit(ATL) pop(SFO)  + ATL
#               -> visit(SFO) , + SFO
#              

from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            print(route)
            
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []
        visit('JFK')
        return route[::-1]


