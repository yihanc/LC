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

# 2018.02.22 
# Faster Approach
# Since len of word is fixed, maintain a Counter by advancing word length
# Also, use compare helper to compare the Counter of words and current words.
from collections import defaultdict
from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total_char = sum(map(lambda t:len(t), words))
        word_len = len(words[0])
        dic, to_check = Counter(words), None
        res = []
        
        for start in xrange(word_len):
            while start + total_char <= len(s):
                if to_check is None:    # Initialize Counter dic by splitting and counting
                    L = [ s[i:i+word_len] for i in xrange(start, start + total_char, word_len) ]
                    to_check = Counter(L)
                else:                   # Update Counter by removing left_most word and adding right_most
                    first_word, last_word = s[start-word_len:start], s[start+total_char-word_len : start+total_char]
                    to_check[first_word] -= 1
                    to_check[last_word] += 1
                    if to_check[first_word] == 0: 
                        del to_check[first_word]        # Remove from dic if count is 0

                if self.compare(dic, to_check) is True:
                    res.append(start)
                start += word_len
            to_check = None
        return res
    
        
    def compare(self, dic, to_check):
        if len(dic) != len(to_check): return False
        for word, cnt in dic.iteritems():
            if word not in to_check:
                return False
        for word, cnt in to_check.iteritems():
            if word not in dic or dic[word] < cnt:
                return False
        return True


# 2018.02.22 Self rewrite
# TLE for the last case

from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        total_char = sum(map(lambda x:len(x), words))
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1

        res = []
        start = 0
        while start + total_char <= len(s):
            to_check = s[start:start+total_char]
            if self.verify(to_check, dic, len(words[0])) is True:
                res.append(start)
            start += 1
        return res
        
    def verify(self, s, dic, len_word):
        start = 0
        while start + len_word <= len(s):
            word = s[start: start + len_word]
            if word not in dic or dic[word] <= 0:
                return False
            else:
                dic[word] -= 1
            start += len_word
        return True






# 2017.04.08 Rewrite Same Template
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s: return []
        n, nw = len(s), len(words[0])
        res = []
        for start in xrange(nw):
            dic = {}
            for word in words:
                dic[word] = dic.get(word, 0) + 1
                
            l, r, count = start, start, 0
            while r <= n:
                #print(l, r, count, dic)
                if count == len(words):
                    if r - l == len(words) * nw: res.append(l)
                    if l + nw <= n:
                        lword = s[l:l+nw]
                        if lword in dic:
                            dic[lword] += 1
                            if dic[lword] > 0: count -= 1
                    l += nw
                    continue
                
                if r + nw <= n:
                    rword = s[r:r+nw]
                    if rword in dic:
                        dic[rword] -= 1
                        if dic[rword] >= 0: count += 1
                r += nw
        return res

# 12.17.2016 Rewrite
# Algorithm:
# dic and cdic, l, r, count
# 1. if r word not dic, move r and l, update count, cdic to empty
# 2. if r word in dic and available. dic[rword]++ and move right. update count, cdic
# 3. if r word in dic but not available. move left one word. and update count, cdic

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        m, n, nw = len(s), len(words), len(words[0])
        res = []

        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        
        for i in xrange(nw):
            cdic = {}
            l, r, count = i, i, 0
            
            while r <= m:
                rword = s[r:r+nw]
                
                if count == n: res.append(l)
                
                if cword not in dic:
                    l = r + nw
                    count = 0
                    cdic = {}
                else:
                    if cword not in cdic or cdic[cword] < dic[cword]:
                        cdic[cword] = cdic.get(cword, 0) + 1
                        count += 1
                    else:
                        if s[l:l+nw] in cdic:
                            cdic[s[l:l+nw]] -= 1
                            count -= 1
                        l += nw
                        continue
                r += nw
        return res

# 11.22.2016 Rewrite
# Idea: 
# 1. Get occurance of each words in tdic.
# 2. l, r for keeping the window. seen{} for current counts. count 
# 3. Loop each word
#  3.1 If matched and available. Move right by 1 word.
#  3.2 If in dic and not available. Move left X times till word is avai
#  3.3 If not in words, move l to r. "0" the seen{}.
#  3.4 If count == len(words), add to result
#
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ns, n = len(s), len(words)
        if ns == 0 or n == 0: return []

        res, wlen = [], len(words[0])
        tdic = {}
        for word in words:  
            if word not in tdic: tdic[word] = 1
            else: tdic[word] += 1

        for i in xrange(wlen):
            l, r, count = i, i + wlen, 0

            seen = { word : 0 for word in words}

            while r <= ns:
                cur_word = s[r-wlen:r]
                if cur_word in seen:
                    if seen[cur_word] < tdic[cur_word]:
                        seen[cur_word] += 1
                        count += 1
                    else:
                       while s[l:l+wlen] != cur_word:
                            seen[s[l:l+wlen]] -= 1
                            count -= 1
                            l += wlen
                       l += wlen
                else:   # Reinitiate
                    l, count = r, 0
                    seen = { word : 0 for word in words }

                if count == n:
                    res.append(l)
                    seen[s[l:l+wlen]] -= 1
                    count -= 1
                    l += wlen

                r += wlen
        return res



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
