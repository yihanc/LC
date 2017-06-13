# 126. Word Ladder II  QuestionEditorial Solution  My Submissions
# Total Accepted: 53420
# Total Submissions: 390450
# Difficulty: Hard
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.

# Algorithm
# Two-end BFS. Use visited, nextlvl to record . build pathmap dic[word] = set([]).
# Then loop through pathMap to get result

from collections import defaultdict
import string
class Solution(object):

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """


if __name__ == "__main__":
    beginWord, endWord = "hit", "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print(Solution().findLadders(beginWord, endWord, wordList))
