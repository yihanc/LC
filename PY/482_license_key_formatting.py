# 482. License Key Formatting   Add to List QuestionEditorial Solution  My Submissions
# Total Accepted: 2649
# Total Submissions: 5876
# Difficulty: Medium
# Contributors: aizj_Forever
# Now you are given a string S, which represents a software license key which we would like to format. The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.
# 
# We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the lower case letters in the string must be converted to upper case.
# 
# So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return the license key formatted according to the description above.
# 
# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
# 
# Output: "24A0-R74K"
# 
# Explanation: The string S has been split into two parts, each part has 4 characters.
# Example 2:
# Input: S = "2-4A0r7-4k", K = 3
# 
# Output: "24-A0R-74K"
# 
# Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could be shorter as said above.
# Note:
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
# String S is non-empty.
# 

# 2017.05.21 
# One loop
from collections import deque
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = len(S)
        res = deque()
        cnt = 0
        tmp = ""
        for i in xrange(n - 1, -1, -1):
            if S[i] == "-": continue
            cnt += 1
            tmp = S[i].upper() + tmp
            if cnt == K:
                res.appendleft(tmp)
                tmp, cnt = "", 0
        if tmp: res.appendleft(tmp)
        return "-".join(res)

# One Pass.
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        n = len(S)
        i = n - 1
        res = ""

        count = 0        
        while i >= 0:
            if S[i] == "-":
                i -= 1
                continue
            
            if count == K:
                res = "-" + res
                count = 0
                continue
            
            res = S[i].upper() + res
            count += 1
            i -= 1
        
        return res

