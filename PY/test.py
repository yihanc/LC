def preprocess(s, val):
    head = ""
    i = 0
    while i < len(s):
        if s[i] not in "()": head = head + s[i]
        elif s[i] == "(": break
        else: val += 1
        i += 1
    print(head)
    
    tail = ""
    j = len(s) - 1
    while j >= i:
        if s[j] not in "()": tail = s[j] + tail
        elif s[j] == ")": break
        else: val -= 1
        j -= 1
    
    print(tail)
    print(i, j, s[i:j+1])
    return [head + s[i:j+1] + tail, val]

s = ")k)))())()())))())"
print(preprocess(s, -9))
