# 1. max num of A
def mx(A):
    return sorted(A)[-1]
    

# 2. Most frequent number
def fre(A):
    dic = {}
    res = None
    for num in A:
        dic[num] = dic.get(num, 0) + 1
    mostfre = 0
    for num, fre in dic.iteritems():
        if fre > mostfre:
            mostfre, res = fre, num 
    return [res, mostfre]
    
# 3. median 
def median(A):
    n, A = len(A), sorted(A)
    if n & 1: return A[n//2]
    else: return (A[n//2] + A[n//2-1]) / 2.0

# 4. Find the minimum absolute differece in the list
import sys
def diffAbs(A):
    if len(A) <= 1: return "ERROR"
    res = sys.maxint
    for i in xrange(len(A) - 1):
        for j in xrange(i + 1, len(A)):
            res = min(res, abs(A[i] - A[j]))
    return res
    
# 5. Find out the first non-duplicate number in the list
from collections import defaultdict
def firstNonDup(nums):
    dic = defaultdict(list)
    for i in xrange(len(nums)):
        dic[nums[i]].append(i)
    
    minIndex = len(nums)
    for k, v in dic.iteritems():
        if len(v) == 1:
            minIndex = min(minIndex, v[0])
    return nums[minIndex] if minIndex != len(nums) else "ERROR"
        
# 6. Find out the Greatest Commmon Divisor 
def gcd(nums):
    n = len(nums)
    if n == 0: return "ERROR"
    if n == 1: return nums[0]
    if n >= 2: return gcd2(gcd(nums[:n//2]), gcd(nums[n//2:]))

def gcd2(n1, n2):
    for num in xrange(min(n1, n2), 0, -1):
        if n1 % num == 0 and n2 % num == 0:
            return num

# 7. Find out the Least Common Multiple
def lcm(nums):
    n = len(nums)
    if n == 0: return "ERROR"
    if n == 1: return nums[0]
    if n >= 2: return lcm2(lcm(nums[:n//2]), lcm(nums[n//2:]))

def lcm2(n1, n2):
    return n1 * n2 / gcd2(n1, n2)
    

import random
if __name__ == "__main__":
    nums = [random.randrange(12, 50) for _ in xrange(0, 4)]
    #nums = [12, 12, 12, 12, 12, 24, 12, 6, 12, 24]
    print(nums)
    print("MAX : " , mx(nums))
    print("FREQUENCY : ", fre(nums))
    print("MEDIAN : ", median(nums))
    print("DIFF ABS : ", diffAbs(nums))
    print("First Non Duplicate : ", firstNonDup(nums))
    print("GCD : ", gcd(nums))
    print("LCM : ", lcm(nums))
    
