# 271. Encode and Decode Strings Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 19887 Total Submissions: 76044 Difficulty: Medium Contributor: LeetCode
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# 
# Machine 1 (sender) has the function:
# 
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
# 
# string encoded_string = encode(strs);
# and Machine 2 does:
# 
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
# 
# Implement the encode and decode methods.
# 
# Note:
# The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
# Hide Company Tags


# 2017.05.22
# Encode: len + / + str
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "/" + s
        print(res)
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "/": j += 1       # Find out size
            
            size = int(s[i:j])
            j += 1                          # j move to the start of string
            res.append(s[j:j+size])
            i = j + le
        return res
