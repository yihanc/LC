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

import copy
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
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        
        for i in xrange(nw):
            cdic = copy.deepcopy(dic)
            l, r = i, i
            count = 0
            
            while r <= m:
                print(l, r, cdic, res)
                cword = s[r:r+nw]
                
                if count == n:
                    res.append(l)
                
                if cword not in cdic:
                    l = r + nw
                    count = 0
                    cdic = copy.deepcopy(dic)
                else:
                    if cdic[cword] > 0:
                        count += 1
                        cdic[cword] -= 1
                    else:
                        if s[l:l+nw] in cdic:
                            cdic[s[l:l+nw]] += 1
                            count -= 1
                        l += nw
                        continue
                        
                r += nw
        return res

if __name__ == "__main__":
#    s = "barfoofoobarthefoobarman"
#    words = ["bar","foo","the"]
#    s = "barfoothefoobarman"
#    words = ["foo", "bar"]
#    s = "wordgoodgoodgoodbestword"
#    words = ["word","good","best","good"]
    s = "faoucbmnvdujheznbntaszqsxicczlagnqbrsnfptbycfapjnkjflbzilemkpotehwvblcsefqgnsxwgkhnvjpgutuhklcosylvjonqtfyiyyegimtfxilrdiantcdncpiofxgaegjcenkobguyqhsupsjkxnxbehrjgxjlespiiazjiviyeaswuegtrexxnogumrfskwcuwbfgynfdpzzmdfhwletbvbvjtcbfydbxhgdfuiilkhznpjmcnhdkjytecujbykafqdkmovaacbntkbwyjziuaeycyhfytfdllqybnabpbqlmujmdiwxkaxnzeuxzcdknvkqimtzojkcdtoiemhonedokanjcswpnihvvaxlljprdfzjrhzgnfwyfkjhchyssfppfmaqwrjbwjmnslwhqsfverejacbshshohjhdaqgwzsmtfkbycitjzasccvukpcywlhboyjkzdyvjiwhngcwicqkhnercgrzuzcizmuyptvadrhqymmgqeqxrwqwfivzjzjklfkbygbczlszzhfpnxpfwfdbpacazlklqxordrveepedwlvmjktfrwihwkjvvugntweyqzcupgynstzdfskwqsfmcpixlqmenrcfsezjlxzdsyiztswjkdymsgldwxhlqlqjqsudptikuqjpihyslwgderjdqsqhejswbmzqihcczorhvrbiqhouaxxqroxvxrragssozvqajhhgakrqrfltekkvajtzbkzhfsvepnfawoiwzznsgammmykphdoipqrukobzbizxyhuxjjsrjgexgomntbyktphdekchsdfqmbqxkkpvstsyjfleilqbdxgjhkqbnvsbwkzguodmjwkubxaljqomouvxelztjtwhdvqzltlwpxssusffjtrznowtavmlojstgisuefsvclozdteopwnckmwmjkzavstecoyitsewduvjpzzexnjkbhykrympsitwwtfpllnrfiaukzzjoivrrueisqxmysiulpmzazqfkqcwrbfilbzcxfmrwmdwelrsbfrdehjqznmsquabxcfuhtlfhqcmbvgeaxkggvxfilxyfabecgalbnrjdtxhodnqcxwisvpahmyomztqhveljvumotteyhuagskzozbxlclabgslcwylruzhnvnlejnkcxlswnpjrajsjefnadauxzbmwrzaamnclauhplrgocbxggkjmkdllgykzzkamzcxazhpkywycxxlfhuttzfhhfrhedjqfnqfmxwzxuxztxmzgischzjrecajhjbmwrtlqqknmjpgg"
    words = ["mntbyktphdekchsdfqmbq","zznsgammmykphdoipqruk","hyssfppfmaqwrjbwjmnsl","hkqbnvsbwkzguodmjwkub","qsqhejswbmzqihcczorhv","xaljqomouvxelztjtwhdv","dptikuqjpihyslwgderjd","sozvqajhhgakrqrfltekk","lszzhfpnxpfwfdbpacazl","tavmlojstgisuefsvcloz","wjkdymsgldwxhlqlqjqsu","dteopwnckmwmjkzavstec","obzbizxyhuxjjsrjgexgo","rwqwfivzjzjklfkbygbcz","whngcwicqkhnercgrzuzc","frwihwkjvvugntweyqzcu","rbiqhouaxxqroxvxrrags","qmenrcfsezjlxzdsyizts","cvukpcywlhboyjkzdyvji","xkkpvstsyjfleilqbdxgj","ykrympsitwwtfpllnrfia","daqgwzsmtfkbycitjzasc","whqsfverejacbshshohjh","oyitsewduvjpzzexnjkbh","izmuyptvadrhqymmgqeqx","klqxordrveepedwlvmjkt","qzltlwpxssusffjtrznow","pgynstzdfskwqsfmcpixl","vajtzbkzhfsvepnfawoiw"]
    
    print(s, words)
    Solution().findSubstring(s, words)
