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
        dic = { 1: "I",
                4: "IV",
                5: "V",
                9: "IX",
                10: "X",
                40: "XL",
                50: "L",
                90: "XC",
                100: "C",
                400: "CD",
                500: "D",
                900: "CM",
                1000: "M" }
        
        res = ""

        # 1000 <= num <= 3999
        while num >= 1000:
            res += "M"
            num -= 1000

        for i in [100, 10, 1]:
            if num >= i * 9:
                res += dic[i*9]
                num -= i * 9
            elif num < i * 9 and num >= i * 5:
                res += dic[i*5]
                num -= i * 5 
            elif num < i * 5 and num >= i * 4:
                res += dic[i*4]
                num -= i * 4

            while num >= i:
                res += dic[i]
                num -= i
            
        return res

# Version 1
# class Solution(object):
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         res = ""
# 
#         # 1000 <= num <= 3999
#         while num >= 1000:
#             res += "M"
#             num -= 1000
# 
#         # num < 1000
#         if num >= 900:
#             res += "CM"
#             num -= 900
#         elif num < 900 and num >= 500:
#             res += "D"
#             num -= 500
#         elif num < 500 and num >= 400:
#             res += "CD"
#             num -= 400
# 
#         while num >= 100:
#             res += "C"
#             num -= 100
# 
#         #  num < 100
#         if num >= 90:
#             res += "XC"
#             num -= 90
#         elif num < 90 and num >= 50:
#             res += "L"
#             num -= 50
#         elif num < 50 and num >= 40:
#             res += "XL"
#             num -= 40
# 
#         while num >= 10:
#             res += "X"
#             num -= 10
#         
#         # num < 10
#         if num >= 9:
#             res += "IX"
#             num -= 9
#         elif num < 9 and num >= 5:
#             res += "V"
#             num -= 5
#         elif num < 5 and num == 4:
#             res += "IV"
#             num -= 4
# 
#         while num >= 1:
#             res += "I"
#             num -= 1
# 
#         return res
