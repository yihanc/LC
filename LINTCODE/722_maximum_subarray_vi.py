# 722. Maximum Subarray VI 
# Given an array of integers. find the maximum XOR subarray value in given array.
# 
# What's the XOR: https://en.wikipedia.org/wiki/Exclusive_or
# 
#  Notice
# Expected time complexity O(n).
# 
# Have you met this question in a real interview? Yes
# Example
# Given nums = [1, 2, 3, 4], return 7
# The subarray [3, 4] has maximum XOR value
# 
# Given nums = [8, 1, 2, 12, 7, 6], return 15
# The subarray [1, 2, 12] has maximum XOR value
# 
# Given nums = [4, 6], return 6
# The subarray [6] has maximum XOR value
# 


# https://threads-iiith.quora.com/Tutorial-on-Trie-and-example-problems
# Algorithm
# F(L,R)=F(1,R) XOR F(1,L-1).

# Python version is getting TLE

class Solution:
    """
    @param: : the array
    @return: the max xor sum of the subarray in a given array
    """

    def maxXorSubarray(self, nums):
        # write code here
        res = float('-inf')
        pre = 0
        trie = Trie()
        #print(trie)
        for num in nums:
            pre = pre ^ num
            #print("Inserting pre, num: ", pre, num)
            trie.insert(pre)
            res = max(res, trie.query(pre))
            #print("res: ", res)
        return res
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.INTBITS = 32

    def insert(self, x):
        iter = self.root
        for i in xrange(self.INTBITS, -1, -1):
            v = int(bool(x & (1 << i)))
#            print("v : ", v)
            if iter.next[v] == 0:
                iter.next[v] = TrieNode()
            iter = iter.next[v]
        iter.val = x

    # When querying, try to find the biggest number that is different from input
    # Every time down the Trie, it tries to find the opposite of current bit of x
    # If can't find, pick the current bit
    # Also, it makes sure this number was inserted before.
    def query(self, x): 
        iter = self.root
        for i in xrange(self.INTBITS, -1, -1):
            v = int(bool(x & (1 << i)))
            #print("iter ", i, v, iter.next)
            tmp = iter          # Complier complains
            if tmp.next[1-v] != 0:
                iter = iter.next[1-v]
            elif tmp.next[v] != 0:
                iter = iter.next[v]
        #print("QUERY result: x, iter.val, x^iter.val :", x, iter.val, x ^ iter.val)
        #print("Bin format: ", bin(x), bin(iter.val), bin(x^iter.val))
        
        return x ^ iter.val


        

class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [0, 0]



with open("./4.txt", "r") as f:
    for line in f:
        line = line[1:-1].strip().split(",")

nums = [ int(x) for x in line ]
print(Solution().maxXorSubarray(nums))
