# 30. Substring with Concatenation of All Words My Submissions QuestionEditorial Solution
# Total Accepted: 55553 Total Submissions: 265245 Difficulty: Hard
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# You should return the indices: [0,9].
# (order does not matter).
#




# Two dic, counts and seen
# Easy but slow
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        counts = { word : 0 for word in words }
        for word in words:
            counts[word] += 1
        n, num, l_word = len(s), len(words), len(words[0])

        for i in xrange(0, n - num*l_word + 1):
            seen = { word: 0 for word in words }

            j = 0
            while j < num:
                word = s[i+j*l_word : i+(j+1)*l_word]
                if word in counts:
                    seen[word] += 1
                    if seen[word] > counts[word]:
                        break
                else:
                    break
                j += 1
            if j == num: res.append(i)
        
        return res

# My solution. Not good.
# 1 Check words[0] in s, record index in res, remove words[0]
# then for each index in res, i+n or i-n, check if the string in the words
# if yes: update res to the start index, count ++, remove the word
# if no, remove the index from res
# repeat until res is empty or words is empty

# Case to remove res[i]:
# 1. if left and right exist but none in words.
# 2. if only right and right not in words or only left and left not in words
#
# Case to update words dic
# 1. if right exist and in dic, update dic, count += 1, res[i]
# 2. if left exist and in dic, update dic, count += 1, res
import unittest

class TestSolution(unittest.TestCase):
    def test_0(self):
        A = Solution().findSubstring("barfoothefoobarman", ["foo","bar"])
        B = [0, 9]
        self.assertEqual(A, B)

#    def test_1(self):
#        A = Solution().findSubstring("barfoothefoobarman", ["foo","bar", "the"])
#        B = [0, 6]
#        self.assertEqual(A, B)

    # This test case failed because it check right first...
    # hmm. so we need to maintain a window. from left to right. for all the possibilities
    # i = 8, n words, each len 2
    # string 1: [0:8]
    # string 2: [2:8] + [10:12]
    # string 3: [4:8] + [10:14]
    # string 4: [6:8] + [10:16]
    # string 5: [10:18]
  
#    def test_2(self):
#        A = Solution().findSubstring("aabbccddeeaaeeddaabbcc", ["ee","dd","cc","aa","bb"])
#        B = [0, 2, 12]
#        self.assertEqual(A, B)

if __name__ == "__main__":
    unittest.main()
