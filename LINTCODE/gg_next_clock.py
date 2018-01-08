
# S in format of "12:34"
# S can be used only once
def nextClock(S):
    def _dfs(line, nums):
        if len(line) == 4:
            if validClock(line):
                mins = getMinutes(line)
                dic.append((mins, line))
            return 
        
        for i in xrange(len(nums)):
            _dfs(line + nums[i], nums[:i] + nums[i+1:])
        
    nums = [ c for c in S if c != ":" ]
    print(nums)
    dic = []
    _dfs("", nums)

    s_dic = sorted(dic, key = lambda x: x[0])
    print s_dic
    cur_min = getMinutes(S[:2] + S[3:])
    for i in xrange(len(s_dic)):
        if cur_min == s_dic[i][0]:
            print(i, s_dic[i])
            if i != len(s_dic) -1:
                return s_dic[i+1][1]
            else:
                return s_dic[0][1]
        
# Format: "1234"
def validClock(time):
    print(time)
    return int(time[:2]) <= 23 and int(time[2:]) <= 59

# Format: "1234"
def getMinutes(time):
    return int(time[:2]) * 60 + int(time[2:])

print ("12:34", nextClock("12:34"))
print ("21:56", nextClock("21:56"))
print ("00:01", nextClock("00:01"))


# print(validClock("1234"))
# print(validClock("2359"))
# print(validClock("0000"))
# print(validClock("2400"))
# print(validClock("2401"))
# print(validClock("0161"))
# print(validClock("0160"))
