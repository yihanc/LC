# 12. Integer to Roman My Submissions QuestionEditorial Solution
# Total Accepted: 65050 Total Submissions: 165700 Difficulty: Medium
# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.
# 
# Subscribe to see which companies asked this question
# Roman
# Symbol    Value
# I   1  I II III IV 
# IV  4 
# V   5  V VI VII VIII IX
# IX  9
# X   10 X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXI XXII XXII XXIII .. 
#        ILI ILII ILIII ILIV ILV ILVI ILVII ILV
# XL  40
# L   50
# XC  90 
# C   100
# CD  400
# D   500
# CM  900
# M   1,000  MMMCM
#
# Anyway to make it shorter?
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
