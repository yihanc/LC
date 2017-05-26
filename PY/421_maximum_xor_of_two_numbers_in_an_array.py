# 421. Maximum XOR of Two Numbers in an Array Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 11759
# Total Submissions: 26357
# Difficulty: Medium
# Contributors:
# shen5630
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.


# 2017.05.26
# bit manipulation
# Forming res from left to right.
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, mask = 0, 0
        for i in xrange(31, -1, -1):
            mask = mask | (1 << i)  # ith bit left -> right
            dic = set()
            for num in nums:
                dic.add(num & mask) # first ith bit of num. element in dic have the same prefix bit
            tmp = res | (1 << i)    # tmp = bin(res) + "1"
            print(res, bin(tmp), dic)
            for prefix in dic:      # Existing nums 
                if tmp ^ prefix in dic: # 
                    res = tmp
                    break           # if no one hit, that means this bit is "0"
        return res

# This algorithm's idea is:
# to iteratively determine what would be each bit of the final result from left to right. And it narrows down the candidate group iteration by iteration. e.g. assume input are a,b,c,d,...z, 26 integers in total. In first iteration, if you found that a, d, e, h, u differs on the MSB(most significant bit), so you are sure your final result's MSB is set. Now in second iteration, you try to see if among a, d, e, h, u there are at least two numbers make the 2nd MSB differs, if yes, then definitely, the 2nd MSB will be set in the final result. And maybe at this point the candidate group shinks from a,d,e,h,u to a, e, h. Implicitly, every iteration, you are narrowing down the candidate group, but you don't need to track how the group is shrinking, you only cares about the final result.
