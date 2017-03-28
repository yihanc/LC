# 71. Simplify Path   QuestionEditorial Solution  My Submissions
# Total Accepted: 66918
# Total Submissions: 284386
# Difficulty: Medium
# Contributors: Admin
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
# 
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".

# 2017.03.23 Shorter
from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        d = deque()
        res = ""
        
        for x in path.split('/'):
            if x != "" and x != "." and x != "..":
                d.append(x)
            elif x == ".." and d:
                d.pop()
                
        return "/" if not d else "/" + "/".join(d)
        

# 2017.03.11 Rewrite
from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        d = deque()
        pathlist = path.split("/")
        res = ""
        
        for path in pathlist:
            if path == "." or path == "" or (not d and path == ".."):
                continue
            elif d and path == "..":
                d.pop()
            else:
                d.append(path)
        
        for path in d:
            res = res + "/" + path
        
        return "/" if not res else res
        

from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        d = deque()
        res = ""
        words = path.split("/")
        for word in words:
            if word == ".." and d:
                d.pop()
                continue
            if word == "" or word == "." or word == "..":
                continue
            d.append(word)      # Err 2: FIFO queue

        print(d)
        if not d:           # Special cornor case
            return "/"
        
        while d:
            res = res + "/" + d.popleft()   # Err 1: forget res, pop from left
        
        return res
        
if __name__ == "__main__":
    print(Solution().simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/"))
    print(Solution().simplifyPath("/a/./b/../../c/"))
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/../"))
    print(Solution().simplifyPath("/abc/..."))
