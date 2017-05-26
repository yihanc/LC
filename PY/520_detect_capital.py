# 520. Detect Capital Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 23027
# Total Submissions: 44004
# Difficulty: Easy
# Contributors:
# love_Fawn
# Given a word, you need to judge whether the usage of capitals in it is right or not.
# 
# We define the usage of capitals in a word to be right when one of the following cases holds:
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
# Example 1:
# Input: "USA"
# Output: True
# Example 2:
# Input: "FlaG"
# Output: False
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

# 2017.05.26
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1: return True
        if word[0].isupper():
            remain = word[1].isupper()
            for j in xrange(1, len(word)):
                if word[j].isupper() != remain: return False
        else:
            for j in xrange(1, len(word)):
                if word[j].isupper(): return False
        return True
