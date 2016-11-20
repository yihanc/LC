# 383. Ransom Note   QuestionEditorial Solution  My Submissions
# Total Accepted: 28844
# Total Submissions: 63544
# Difficulty: Easy
# Contributors: Admin
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# 
# Each letter in the magazine string can only be used once in your ransom note.
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for char in magazine:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        
        for char in ransomNote:
            if char not in dic:
                return False
            
            if char in dic and dic[char] <= 0:
                return False
                
            dic[char] -= 1

        return True
