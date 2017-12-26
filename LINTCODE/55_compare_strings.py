# 55. Compare Strings 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Compare two strings A and B, determine whether A contains all of the characters in B.
# 
# The characters in string A and B are all Upper Case letters.
# 
#  Notice
# 
# The characters of B in A are not necessary continuous or ordered.
# 
# Have you met this question in a real interview? Yes
# Example
# For A = "ABCD", B = "ACD", return true.
# 
# For A = "ABCD", B = "AABC", return false.


# 2017.12.11

from collections import defaultdict
class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        if A is None or B is None: return False
        if len(B) == 0: return True
        if len(A) == 0: return False
        dic = defaultdict(int)
        for char in A:
            dic[char] += 1
        
        for char in B:
            dic[char] -= 1
            if dic[char] < 0: return False
        
        return True
