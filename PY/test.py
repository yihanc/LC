class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0: return []
        
        n, start = len(words), 0
        cur_len = 0
        res = []
        
        i = 0
        while i < n:
            cur_len = len(words[i])
            j = i + 1
            while j < n and cur_len + len(words[j]) + 1 <= L:
                cur_len += len(words[j]) + 1
                j += 1
            j -= 1
            
            if j != n - 1:  # not last line
                spaces = (L - cur_len) // (j - i)
                count = (L - cur_len) % (j - i)
                line = ""
                for k in xrange(i, j):
                    line += words[k] + " " * (n + 1)
                    if count > 0:
                        line += " "
                        count -= 1
                res.append(line + words[j])
            else:
                res.append(" ".join(words[i:]))
            i = j + 1
            
        return res

if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    print(Solution().fullJustify(words, L))
