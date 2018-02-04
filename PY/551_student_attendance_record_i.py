# 551. Student Attendance Record I Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 8666
# Total Submissions: 19745
# Difficulty: Easy
# Contributors:
# fallcreek
# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# 
# You need to return whether the student could be rewarded according to his attendance record.
# 
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False

# 2018.01.21
# Rewrite
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenA = False
        
        for i in xrange(len(s)):
            char = s[i]
            if seenA and char == "A": return False
            if i >= 2 and s[i-2:i+1] == "LLL": return False
            seenA = True if char == "A" else seenA
        return True
                
            

# 2017.05.25
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A, L = False, 0
        for i, char in enumerate(s):
            if char == 'A':
                if A: return False
                else: A = True
            elif char == 'L' and (i == 0 or s[i-1] != 'L'):
                L = 1
            elif char == 'L':
                L += 1
                if L > 2: return False
        return True
