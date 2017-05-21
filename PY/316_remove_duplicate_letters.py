# 316. Remove Duplicate Letters Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 28480
# Total Submissions: 97932
# Difficulty: Hard
# Contributor: LeetCode
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
# 
# Example:
# Given "bcabc"
# Return "abc"
# 
# Given "cbacdcbc"
# Return "acdb"

#  Recursive o(26n) solution
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        cnt = {}
        for char in s:
            cnt[char] = cnt.get(char, 0) + 1
        pos = 0
        for i, x in enumerate(s):
            if x < s[pos]: pos = i
            cnt[x] -= 1
            if cnt[x] == 0: break
        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))

# Stack method
# https://www.hrwhisper.me/leetcode-remove-duplicate-letters/
# 首先对字符串出现的个数进行统计。
# 然后对字符串扫描，每遇到一个字符串，判断其是否在栈中，如果在则跳过。（计数 – 1）
# 如果不在栈中，和栈顶的元素判断，要是当前栈顶的元素比较大而且cnt不为0（也就是说之后还有这个元素），就把栈顶弹出。然后把当前的元素入栈。
Python

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        vis, cnt = [False] * 26, [0] * 26
        ans = []
        for c in s:
            cnt[ord(c) - 97] += 1  # ord(a) =97
        for c in s:
            index = ord(c) - 97
            cnt[index] -= 1
            if vis[index]: continue
            while ans and ans[-1] > c and cnt[ord(ans[-1]) - 97]:
                vis[ord(ans.pop()) - 97] = False
            ans.append(c)
            vis[index] = True

        return ''.join(ans)


