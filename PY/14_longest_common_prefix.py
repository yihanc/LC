# 14. Longest Common Prefix My Submissions QuestionEditorial Solution
# Total Accepted: 101848 Total Submissions: 358366 Difficulty: Easy
# Write a function to find the longest common prefix string amongst an array of strings.
# 
# Subscribe to see which companies asked this question

# 11.19.2016
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        cur_char = ""
        
        i = 0
        while len(strs) > 0 and i < len(strs[0]):
            for str in strs:
                if i >= len(str) or (cur_char and cur_char != str[i]):     #Bug
                    return res
                    
                if not cur_char:
                    cur_char = str[i]

            res += cur_char
            cur_char = ""
            i += 1
            
        return res




class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Special case
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        res = ""
        cmpStr = strs[0]
        
        for index, char in enumerate(cmpStr):
            # Compare to each string strs[j]
            j = 1
            while j < len(strs):
                if index >= len(strs[j]) or cmpStr[index] != strs[j][index]:
                    return res
                j += 1
            res += char
        
        return res
