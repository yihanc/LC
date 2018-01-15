def isPal(s):
    print(s)
    l, r = 0, len(s) - 1
    while l < r and s[l] == s[r]:
        l, r = l + 1, r - 1
    return l > r if len(s) % 2 == 0 else l == r

print(isPal("a"))
print(isPal("b"))
print(isPal(""))
print(isPal("ab"))
print(isPal("aaa"))
print(isPal("aba"))
print(isPal("abba"))
print(isPal("abcba"))
print(isPal("abc"))
print(isPal("abcd"))
print(isPal("abcda"))
