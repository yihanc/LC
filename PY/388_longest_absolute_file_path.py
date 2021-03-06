# 388. Longest Absolute File Path Add to List
# DescriptionHintsSubmissionsSolutions
# Total Accepted: 27262
# Total Submissions: 76007
# Difficulty: Medium
# Contributor: LeetCode
# Suppose we abstract our file system by a string in the following manner:
# 
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# 
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# 
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# 
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
# 
# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).
# 
# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.
# 
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
# 
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
# 
# Subscribe to see which companies asked this question.


# 2017.06.1
# Self rewrite
from collections import deque
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        A = input.split('\n')
        #print(A)
        d = deque()
        res = 0
        for i in xrange(len(A)):
            index = A[i].rfind('\t')
            #print(A[i], index)
            while d and index - d[-1][0]  < 1:    # pop
                d.pop()
            lastlen = 0 if not d else d[-1][1]
            d.append([index, lastlen + len(A[i]) - index - 1])
            #print(d)
            if "." in A[i]: 
                res = max(res, d[-1][1] + index + 1)    # RES has index + 1 "/"
        return res
            
                

# 2017.05.11 online resolution
from collections import deque
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        d = deque()
        d.append(0)
        res = 0
        for s in input.split("\n"):
            lev = s.rfind("\t") + 1     # note that len("\t") == 1 not 2
            while lev + 1 < len(d):
                d.pop()
            clen = d[-1] + len(s) - lev + 1
            d.append(clen)
            if "." in s: res = max(res, clen - 1)
        return res
