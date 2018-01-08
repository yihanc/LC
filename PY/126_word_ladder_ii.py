# 126. Word Ladder II  QuestionEditorial Solution  My Submissions
# Total Accepted: 53420
# Total Submissions: 390450
# Difficulty: Hard
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.




# 2017.12.28 Build Map for parents + BFS from [END]
# Step 1, calculate parents map from start to end
# Step 2, based on parents map build results from end to start
# Optimizatino, Using list comprehension for step 2 is much faster

from collections import defaultdict
import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if len(beginWord) != len(endWord): return []
        dict = set(wordList)
        if endWord not in dict: return []
        
        parents = defaultdict(set)
        level = {beginWord}
        
        while level and endWord not in parents:
            next_level = defaultdict(set)
            
            for word in level:
                for i in xrange(len(word)):
                    for char in string.ascii_lowercase:
                        next_word = word[:i] + char + word[i+1:]
                        if next_word in dict and next_word not in parents:
                            next_level[next_word].add(word)
            
            parents.update(next_level)
            level = next_level
        
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [ [p] + line for line in res for p in parents[line[0]]]
        return res
        
        
# 2016.02.22, Two-end BFS. 
# Note:
# wordList is now a list. Convert to set() for fast query. if endWord not in wordList, return []
# Remove word from wordList outside the loop. No visisted[]
# Use line + [word] to generate line
import string
from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList: return []   # Bug 1
        wordList = set(wordList)
        beginSet, endSet = set([beginWord]), set([endWord])
        if beginWord in wordList: wordList.remove(beginWord)
        if endWord in wordList: wordList.remove(endWord)
        
        mp = defaultdict(list)
        depFound = False
        while beginSet and endSet:
            if len(beginSet) < len(endSet):
                isBeginSmall, small, big = True, beginSet, endSet
            else:
                isBeginSmall, small, big = False, endSet, beginSet
                
            nextlvl = set([])
            
            for word in small:
                for i in xrange(len(word)):
                    for char in string.ascii_lowercase:
                        tmp = word[:i] + char + word[i+1:]
                        
                        if tmp in big:
                            depFound = True
                        
                        if tmp in wordList or tmp in big:   # Bug 2. If missing tmp in big. Mp{} is missing entry
                            nextlvl.add(tmp)
                        
                            if isBeginSmall:
                                mp[word].append(tmp)
                            else:
                                mp[tmp].append(word)
            
            if depFound: break
        
            for word in nextlvl:                    # Bug 3. If remove word inside the loop. Missing Map entry
                wordList.remove(word)
        
            if isBeginSmall: beginSet = nextlvl
            else: endSet = nextlvl
        
        if not depFound: return []
        
        res = [[beginWord]]
        while res[0][-1] != endWord:
            print(res)
            tmp = res
            res = []
            for line in tmp:
                nextWords = mp[line[-1]]
                for word in nextWords:
                    res.append(line + [word])       # Bug 4. Use line + [word] to create new line
        
        return res
                            
                        

# 12.6.2016, Two-end BFS. 

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        beginSet, endSet = set([beginWord]), set([endWord])
        if beginWord in wordlist: wordlist.remove(beginWord)
        if endWord in wordlist: wordlist.remove(endWord)
        ATOZ = "abcdefghijklmnopqrstuvwxyz"
        depFound = False
        pathMap = {}

        while beginSet and endSet:
            if len(beginSet) < len(endSet):
                isBeginSmall, small, big = True, beginSet, endSet
            else:
                isBeginSmall, small, big = False, endSet, beginSet

            nextlvl = set([])

            for word in small:
                for i in xrange(len(word)):
                    for char in ATOZ:
                        newword = word[:i] + char + word[i+1:]
                        
                        if newword in big:
                            depFound = True

                        if newword in big or newword in wordlist:   #Update pathMap
                            nextlvl.add(newword)
                            if word not in pathMap:
                                pathMap[word] = set([])
                            if newword not in pathMap:
                                pathMap[newword] = set([])

                            if isBeginSmall:
                                pathMap[word].add(newword)
                            else:
                                pathMap[newword].add(word)

            if depFound: break
        
            for word in nextlvl:
                wordlist.remove(word)
                                    
            if isBeginSmall: beginSet = nextlvl
            else: endSet = nextlvl
        
        if not depFound: return []

        res = []                # Generate RES from pathMap
        res.append([beginWord])    
        while res[0][-1] != endWord:
            tmp = res
            res = []
            for line in tmp:
                for newword in pathMap[line[-1]]:
                    newline = line + [newword]
                    res.append(newline)

        return res

            
if __name__  == "__main__":
    start = "qa"
    end = "sq"
    dic = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

#    start = "a"
#    end = "c"
#    dic = ["a", "b", "c"]

#    start = "hot"
#    end = "dog"
#    dic = ["hot","dog","dot"]

#    start = "red"
#    end = "tax"
#    dic = ["ted","tex","red","tax","tad","den","rex","pee"]

    Solution().findLadders(start, end, dic)




#    start = "cet"
#    end = "ism"
#    dic = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
#    Solution().findLadders(start, end, dic)




# from collections import deque
# import copy
# 
# class Solution(object):
#     def findLadders(self, beginWord, endWord, wordlist):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordlist: Set[str]
#         :rtype: List[List[int]]
#         """
#         wordlist.remove(beginWord)
#         tmpList = copy.deepcopy(wordlist)
#         maxDep = self.ladderLength(beginWord, endWord, tmpList)
#         print(maxDep)
#         print(wordlist)
#         res = []
#         atoz = 'abcdefghijklmnopqrstuvwxyz'
# 
#         def dfs(dep, line, wordlist):
#             if dep >= maxDep:
#                 return
#             
#             cur = line[-1]
#             
#             for i in xrange(len(cur)):
#                 for char in atoz:
#                     if cur[i] == char:
#                         continue
#                     
#                     replaced = cur[:i] + char + cur[i+1:]
#                     if replaced == endWord:                  
#                         print(dep)
#                         res.append(line + [replaced])
#                         continue
#                     
#                     if replaced in wordlist:
#                         newWordList = copy.deepcopy(wordlist)
#                         newWordList.remove(replaced)
#                         dfs(dep+1, line + [replaced], newWordList)
#             
#         dfs(1, [beginWord], wordlist)
#         print(res)
#         return res
# 
#     
#     def ladderLength(self, beginWord, endWord, wordList):
#         d = deque()
#         d.append([beginWord, 1])
#         atoz = 'abcdefghijklmnopqrstuvwxyz'
# 
#         while d:
#             cur = d.pop()
#             curWord, curDep, tmpList = cur[0], cur[1], []
#             
#             for i in xrange(len(curWord)):
#                 for char in atoz:
#                     if curWord[i] == char:
#                         continue
#                     
#                     replaced = curWord[:i] + char + curWord[i+1:]
#                     if replaced == endWord:
#                         return curDep + 1
#                         
#                     if replaced in wordList:
#                         d.appendleft([replaced, curDep + 1])
#                         wordList.remove(replaced)
#         return 0
