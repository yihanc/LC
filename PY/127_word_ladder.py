# 127. Word Ladder  QuestionEditorial Solution  My Submissions
# Total Accepted: 93587
# Total Submissions: 480960
# Difficulty: Medium
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
# 
# Only one letter can be changed at a time
# Each intermediate word must exist in the word list
# For example,
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# Subscribe to see which companies asked this question

# 2017.02.22 Rewrite 2way BFS. Changes to questions
# wordList is now a list but not set. So "word" in wordList is very slow now
# endWord has to be in the wordList
# No visited. Remove from wordList outside the loop
import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        wordList = set(wordList)
        beginSet, endSet = set([beginWord]), set([endWord])
        #wordList.remove(beginWord)
        wordList.remove(endWord)

        dep = 1        
        while beginSet and endSet:
            if len(beginSet) < len(endSet):
                isBeginSmall, small, big = True, beginSet, endSet
            else:
                isBeginSmall, small, big = False, endSet, beginSet
            
            nextlvl = set([])
            dep += 1
            for word in small:
                for i in xrange(len(word)):
                    for char in string.ascii_lowercase:
                        newWord = word[:i] + char + word[i+1:]
                        
                        if newWord in big:
                            return dep
                        
                        if newWord in wordList:
                            nextlvl.add(newWord)
            
            for word in nextlvl:
                wordList.remove(word)
                
            if isBeginSmall: beginSet = nextlvl
            else: endSet = nextlvl
            
        return 0


# 12.04.2016 Rewrite. 2way BFS
# Why set?

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        res = 1
        beginSet, endSet, visited = set([beginWord]), set([endWord]), set([beginWord, endWord])
        atoz = "abcdefghijklmnopqrstuvwxyz"
        
        while beginSet and endSet:
            isBeginSetSmall = False
            if len(beginSet) < len(endSet): isBeginSetSmall = True
            
            if isBeginSetSmall:
                small, big = beginSet, endSet
            else:
                small, big = endSet, beginSet
            
            next = set([])
            res += 1
            print(beginSet, endSet, visited)
            
            for word in small:
                for i in xrange(len(word)):
                    for char in atoz:
                        tmp = word[:i] + char + word[i+1:]
                        if tmp in big: 
                            return res
                        
                        if tmp in wordList and tmp not in visited:
                            visited.add(tmp)
                            next.add(tmp)
            
            if isBeginSetSmall:
                beginSet = next
            else:
                endSet = next
        
        return 0
        

# notes:
# 1. Don't iterate over dict. Get TLE
# 2. Remove beginWord from wordList

from collections import deque

class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.remove(beginWord)

        d = deque()
        d.append([beginWord, 1])
        atoz = 'abcdefghijklmnopqrstuvwxyz'

        while d:
            cur = d.pop()
            curWord, curDep = cur[0], cur[1]
            
            for i in xrange(len(curWord)):
                for char in atoz:
                    if curWord[i] == char:
                        continue
                    
                    replaced = curWord[:i] + char + curWord[i+1:]
                    if replaced == endWord:
                        return curDep + 1
                        
                    if replaced in wordList:
                        print([replaced, curDep + 1])
                        d.appendleft([replaced, curDep + 1])
                        wordList.remove(replaced)
        return 0
    

if __name__  == "__main__":
    # start = "game"
    # end = "thee"
    # dic = ["frye","heat","tree","thee","game","free","hell","fame","faye"]
    start = "cet"
    end = "ism"
    dic = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    print(Solution().ladderLength(start, end, dic))
