# 13. Roman to Integer My Submissions QuestionEditorial Solution
# Total Accepted: 86459 Total Submissions: 217178 Difficulty: Easy
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = { "M": 1000
                "CM": 900
                "D": 500
                "CD": 400
                "C": 100
                "XC": 90
                "L": 50
                "XL": 40
                "X": 10
                "IX": 9
                "V": 5
                "IV": 4
                "I": 1 }

        res, i = 0, 0
        while i < len(s):
            # Handling special cases for CM, CD, XC, XL, IX, IV
            if i + 1 < len(s) and s[i:i+2] in ["CM", "CD", "XC", "XL", "IX", "IV"]:
                res += dic[s[i:i+2]]
                i += 2
                continue
            
            # Handling other cases
            if s[i] in ["M", "C", "X", "I", "D", "L", "V"]:
                res += dic[s[i]]
                i += 1

        return res
