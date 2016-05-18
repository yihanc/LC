# content of test_sample.py
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""

    #1 Preprocessing abba -> "#a#b#b#a#"
    new_s = "^#" + "#".join(list(s)) + "#$"
    
    #2 l, r, c, i_mirror, i
    center, right, = 0, 0
    P = [0 for x in new_s]

    i = 1
    while i < len(new_s) - 1:
        i_mirror = 2 * center - i
        if right > i:
            P[i] = min(right - i, P[i_mirror])
        
        while new_s[i + P[i] + 1] == new_s[i - P[i] - 1]:
            P[i] += 1

        if i + P[i] > right:
            center = i
            right = i + P[i]
        
        i += 1

    # Iterate again to get the sub string
    mx = max(P)
    center = P.index(mx)
    return new_s[center-mx:center+mx+1].replace("#", "")

if __name__ == "__main__":
    print(longestPalindrome("abba"))
    print(longestPalindrome("a"))
    print(longestPalindrome("ab"))
    print(longestPalindrome("abc"))
    print(longestPalindrome("abcdbac"))
    print(longestPalindrome("babcbabcbaccba"))
