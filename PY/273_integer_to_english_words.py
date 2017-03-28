# 273. Integer to English Words Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 32457
# Total Submissions: 151268
# Difficulty: Hard
# Contributors: Admin
# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
# 
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        return self.helper(num)
    
    def helper(self, num):
        belowTwenty = [ "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", \
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", \
                    "Sixteen", "Seventeen", "Eighteen", "Nineteen" ]
        belowHundred = [ "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety" ]
        
        res = ""
        
        if num < 20: 
            result = belowTwenty[num]
        elif num < 100: 
            result = belowHundred[num // 10 - 2] + " " + belowTwenty[num % 10]
        elif num < 1000: 
            result = belowTwenty[num // 100] + " Hundred " + self.helper(num % 100)
        elif num < 10**6: 
            result = self.helper(num // 1000) + " Thousand " + self.helper(num % 1000)
        elif num < 10**9: 
            result = self.helper(num // 10**6) + " Million " + self.helper(num % 10**6)
        else: 
            result = self.helper(num // 10**9) + " Billion " + self.helper(num % 10**9)
            
        return result.strip()

