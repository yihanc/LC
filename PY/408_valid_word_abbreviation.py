# 408. Valid Word Abbreviation Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 9268
# Total Submissions: 33456
# Difficulty: Easy
# Contributor: LeetCode
# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
# 
# A string such as "word" contains only the following valid abbreviations:
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".
# 
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
# 
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
# 
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
# 
# Return false.


# 2017.05.23
# self wrote

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while j < len(abbr) and i < len(word):
            if abbr[j] in "0123456789":
                if abbr[j] == "0": return False
                k = j
                while k < len(abbr) and abbr[k] in "0123456789":
                    k += 1
                le = int(abbr[j:k])
                if i + le > len(word): return False
                i, j = i + le, k
            else:
                if i < len(word) and word[i] != abbr[j] :
                    return False
                i, j = i + 1, j + 1
        return i == len(word) and j == len(abbr)
