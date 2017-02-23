# 204. Count Primes Add to List
# Description  Submission  Solutions
# Total Accepted: 100916
# Total Submissions: 385094
# Difficulty: Easy
# Contributors: Admin
# Description:
# 
# Count the number of prime numbers less than a non-negative number, n.
# 
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
# 
# Show Hint 
# Subscribe to see which companies asked this question.

# Better
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [ False for x in xrange(n+1) ]
        count = 0
        for i in xrange(2, n):
            if not nums[i]:
                count += 1
                j = 2
                while i * j < n:
                    nums[i*j] = True
                    j += 1
        return count
                    
        


# TLE naive solution
class Solution(object):
    def isPrime(self, n):
        if n < 2: return False
        if n <= 3: return True
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True
    
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        tmp = n - 1
        while tmp >= 2:
            if self.isPrime(tmp):
                count += 1
            tmp -= 1
        return count
