# 28. Implement strStr() My Submissions QuestionEditorial Solution
# Total Accepted: 108909 Total Submissions: 433190 Difficulty: Easy
# Implement strStr().
# 
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# Subscribe to see which companies asked this question

# Other fast algorithms available (KMP, Sunny)

# 2018.04.07
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(haystack), len(needle)
        if n > m: return -1
        if n == 0: return 0
        for i in range(m):
            if haystack[i] == needle[0] and needle == haystack[i:i+n]:
                return i
        return -1

# Naive algorithms
# Careful: "" needle, return 0
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "": return -1

        for i,char in enumerate(haystack):
            print(char + " " + haystack[i:i+len(needle)])
            if char == needle[0] and haystack[i:i+len(needle)] == needle:
                return i

        return -1
                
if __name__ == "__main__":
    A = "aaa"
    B = "a"
    print(Solution().strStr(A, B))
