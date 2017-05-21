# 246. Strobogrammatic Number Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 24570
# Total Submissions: 62312
# Difficulty: Easy
# Contributor: LeetCode
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# 
# For example, the numbers "69", "88", and "818" are all strobogrammatic.

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dic = { "6": "9", "9": "6" }
        i, j = 0, len(num) - 1
        while i <= j:       # <= not <, different with Palidrome
            if ( ( num[i] in "018" and num[i] == num[j] ) or 
                ( num[j] in dic and num[i] == dic[num[j]] ) ):
                i, j = i + 1, j - 1
            else:
                return False
        return True
                

