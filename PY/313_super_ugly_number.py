# 313. Super Ugly Number Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 34492
# Total Submissions: 92506
# Difficulty: Medium
# Contributor: LeetCode
# Write a program to find the nth super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.
# 
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question.


# 2017.05.13 
# 1816ms. super slow
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [ float('inf') for x in xrange(n) ]
        idx = [ 0 for x in xrange(len(primes)) ]
        ugly[0] = 1
        for i in xrange(1, n):
            for j in xrange(len(primes)):
                if primes[j] * ugly[idx[j]] == ugly[i-1]:
                    idx[j] += 1
                ugly[i] = min(ugly[i], primes[j] * ugly[idx[j]])
        return ugly[n-1]
        
