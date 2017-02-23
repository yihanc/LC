# 165. Compare Version Numbers Add to List
# Description  Submission  Solutions
# Total Accepted: 77916
# Total Submissions: 401269
# Difficulty: Medium
# Contributors: Admin
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
# 
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
# 
# Here is an example of version numbers ordering:
# 
# 0.1 < 1.1 < 1.2 < 13.37

# Best solution
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        n = max(len(v1), len(v2))
        i = 0
        while i < n:
            num1 = int(v1[i]) if i < len(v1) and v1[i] != "" else 0
            num2 = int(v2[i]) if i < len(v2) and v2[i] != "" else 0
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                i += 1
        return 0


class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Remove "0" and "" from end.
        i = len(v1) - 1
        while i >= 0 and (v1[i] == "" or int(v1[i]) == 0):
            del v1[i]
            i -= 1
            
        j = len(v2) - 1
        while j >= 0 and (v2[j] == "" or int(v2[j]) == 0):
            del v2[j]
            j -= 1
        
        n1, n2 = len(v1), len(v2)

        i = 0
        while i < n1:
            if i >= n2: return 1
            
            if int(v1[i]) == int(v2[i]):
                i += 1
                continue
            elif ((v1[i] != "" and v2[i] == "") or 
                (v1[i] != "" and v2[i] != "" and int(v1[i]) > int(v2[i]))):
                return 1
            else:
                return -1
        
        if i == n2:
            return 0
        else:
            return -1
                        
            
