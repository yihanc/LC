# 288. Unique Word Abbreviation Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 25079
# Total Submissions: 155143
# Difficulty: Medium
# Contributor: LeetCode
# An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:
# 
# a) it                      --> it    (no abbreviation)
# 
#      1
# b) d|o|g                   --> d1g
# 
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
# 
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
# 
# Example: 
# Given dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> 
# false
# 
# isUnique("cart") -> 
# true
# 
# isUnique("cane") -> 
# false
# 
# isUnique("make") -> 
# true

# Some additional clarification to the question
# EX:
# 
# 1) [“dog”]; isUnique(“dig”);   
# //False, because “dig” has the same abbreviation with “dog" and “dog” is already in the dictionary. It’s not unique.
# 
# 2) [“dog”, “dog"]; isUnique(“dog”);  
# //True, because “dog” is the only word that has “d1g” abbreviation.
# 
# 3) [“dog”, “dig”]; isUnique(“dog”);   
# //False, because if we have more than one word match to the same abbreviation, this abbreviation will never be unique.


# 2017.05.22
# Simple dic + set 
# Note that

class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = {}
        for word in dictionary:
            if not word: continue   # Skip empty
            key = word if len(word) == 1 else word[0] + str(len(word)-2) + word[-1]
            if key not in self.dic: 
                self.dic[key] = set()
            self.dic[key].add(word)
        #print(self.dic)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = word if len(word) <= 1 else word[0] + str(len(word) - 2) + word[-1] 
        if ( key not in self.dic or 
            ( key in self.dic and word in self.dic[key] and len(self.dic[key]) == 1 ) ):
            return True
        return False
        
