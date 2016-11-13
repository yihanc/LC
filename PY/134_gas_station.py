# 134. Gas Station   QuestionEditorial Solution  My Submissions
# Total Accepted: 72748
# Total Submissions: 256809
# Difficulty: Medium
# Contributors: Admin
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# 
# Note:
# The solution is guaranteed to be unique.
# 
# Subscribe to see which companies asked this question

# Algorithm:
# 1. Traverse. Record sum_gas and sum_cost and tank
# 2. Anytime, if tank goes negative, start = i+1, tank to 0
# 3. If sum_gas < sum_cost. return -1
#
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, tank, sum_gas, sum_cost = 0, 0, 0, 0
        for i in xrange(len(gas)):
            sum_gas, sum_cost = sum_gas + gas[i], sum_cost + cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
            
        if sum_gas < sum_cost:
            return -1
        else:
            return start
