# 78. Longest Common Prefix 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given k strings, find the longest common prefix (LCP).
# 
# Have you met this question in a real interview? Yes
# Example
# For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
# 
# For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"


# 2017.12.11
class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        res = ""

        i = 0
        while i < len(strs[0]):
            candidate = strs[0][i]
            j = 1
            while j < len(strs):
                if len(strs[j]) <= i or (strs[j][i] != candidate): 
                    return res
                j += 1
            res += candidate
            i += 1
        return res
