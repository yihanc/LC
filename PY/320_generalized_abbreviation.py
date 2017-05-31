# 320. Generalized Abbreviation Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 20612 Total Submissions: 46416 Difficulty: Medium Contributor: LeetCode
# Write a function to generate the generalized abbreviations of a word.
# 
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# 2017.05.26
# DFS backtracking

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def dfs(pos, cur, count):
            if pos == len(word):
                if count > 0: cur += str(count)
                res.append(cur)
                return
            
            dfs(pos + 1, cur, count + 1)    # case 1, deleting more
            if count == 0:                  # case 2, start from 0
                dfs(pos + 1, cur + word[pos], 0)
            else:
                dfs(pos + 1, cur + str(count) + word[pos], 0)
        
        res = []
        dfs(0, "", 0)
        return res
                
            
