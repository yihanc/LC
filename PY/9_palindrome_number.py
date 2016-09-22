# 9. Palindrome Number My Submissions QuestionEditorial Solution
# Total Accepted: 124067 Total Submissions: 389258 Difficulty: Easy
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# 
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.
# 
# Subscribe to see which companies asked this question
# 
# Show Tags
# Show Similar Problems
# 
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        sum = 0
        while x > sum:
            sum = sum * 10 + x % 10
            x = x // 10
        
        return sum == x or (sum // 10 == x)