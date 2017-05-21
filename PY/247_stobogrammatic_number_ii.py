# 247. Strobogrammatic Number II Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 20044
# Total Submissions: 51223
# Difficulty: Medium
# Contributor: LeetCode
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# For example,
# Given n = 2, return ["11","69","88","96"].

# 2017.05.20
# First generate all pairs
# BFS. Similar to phone number
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        nums = [ "0", "1", "6", "8", "9" ]  # Note that "0" Can't be the first or last
        dic = { "0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        res = [["", ""]]
        for i in xrange(n // 2):
            tmp = res
            res = []
            for prefix, postfix in tmp:
                for char in nums:
                    if char == "0" and len(prefix) == 0:
                        continue
                    res.append([prefix + char, dic[char] + postfix])
        tmp = res
        res = []
        for prefix, postfix in tmp:
            if n & 1 == 1:
                for char in ["0", "1", "8"]:
                    res.append(prefix + char + postfix)
            else:
                res.append(prefix + postfix)
        return res
            
