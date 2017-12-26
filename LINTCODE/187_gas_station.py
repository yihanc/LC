class Solution:
    """
    @param: gas: An array of integers
    @param: cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        tank, sum_gas, sum_cost = 0, 0, 0
        start = 0
        i, n = 0, len(gas)
        while i < n:
            tank += gas[i] - cost[i]
            sum_gas += gas[i]
            sum_cost += cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
            i += 1
        return -1 if sum_gas < sum_cost else start
