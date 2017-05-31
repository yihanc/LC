# 465. Optimal Account Balancing Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 3431
# Total Submissions: 10029
# Difficulty: Hard
# Contributors:
# vulkum
# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
# 
# Given a list of transactions between a group of people, return the minimum number of transactions required to settle the debt.
# 
# Note:
# 
# A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
# Person's IDs may not be linear, e.g. we could have the persons 0, 1, 2 or we could also have the persons 0, 2, 6.
# Example 1:
# 
# Input:
# [[0,1,10], [2,0,5]]
# 
# Output:
# 2
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #2 gave person #0 $5.
# 
# Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.
# Example 2:
# 
# Input:
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 
# Output:
# 1
# 
# Explanation:
# Person #0 gave person #1 $10.
# Person #1 gave person #0 $1.
# Person #1 gave person #2 $5.
# Person #2 gave person #0 $5.
# 
# Therefore, person #1 only need to give person #0 $4, and all debt is settled.

# 2017.05.28
# DFS + debt
from collections import defaultdict
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        def dfs(s, cnt):    # s is the start of debt[] index, cnt transaction
            while s < len(debt) and debt[s] == 0:
                s += 1
            res = float('inf')
            prev = 0        # Optimizing. Prev to skip duplicate debt[i]. 
            for i in xrange(s+1, len(debt)):
                if debt[i] != prev and debt[i] * debt[s] < 0:   # find something not the same sign
                    debt[i] += debt[s]      # backtracking
                    res = min(res, dfs(s+1, cnt+1))
                    debt[i] -= debt[s]
                    prev = debt[i]
            return res if res < float('inf') else cnt
            
        bal = defaultdict(int)
        for p1, p2, amt in transactions:
            bal[p1] -= amt
            bal[p2] += amt
        
        debt = []
        for k, v in bal.iteritems():
            if v != 0: debt.append(v)
        return dfs(0, 0)

# cases
# [[0,1,1],[1,2,1],[2,0,1]]
# expected 0

# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 1

