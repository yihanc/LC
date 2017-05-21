# 276. Paint Fence Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 21795
# Total Submissions: 63706
# Difficulty: Easy
# Contributor: LeetCode
# There is a fence with n posts, each post can be painted with one of the k colors.
# 
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# 
# Return the total number of ways you can paint the fence.
# 
# Note:
# n and k are non-negative integers.

# 2017.05.20
# Online better approach
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0: return 0
        if n == 1: return k
        if n == 2: return k * k
        a, b = k, k * (k - 1)
        for i in xrange(3, n + 1):
            a, b = b, a * (k - 1) + b * (k - 1)
        return a + b
        
        # Notes
        # a = same color counts for example: aa, bb, cc
        # b = diff color counts, ab, ac, ba, bc, ca, cb
        # To get next b: b = a * (k - 1),  (they can't use the same char so only k - 1 possible ways)
        #                   + b * (k - 1),  (remaining possible ways (b -a) can have k possible ways each)

# 2017.05.20
# Self wrote
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0: return 0
        if n == 1: return k
        if n == 2: return k * k
        a, b = k, k * k     
        for i in xrange(3, n + 1):
            a, b = b - a, a * (k - 1) + (b - a) * k
        return b
        
        # Notes
        # a = num last two char is the same. for example: aa, bb, cc
        # b is the current answer
        # To get next b: b = a * (k - 1),  (they can't use the same char so only k - 1 possible ways)
        #                   + (b - a) * k,  (remaining possible ways (b -a) can have k possible ways each)
