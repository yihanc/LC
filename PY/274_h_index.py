# 274. H-Index Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 66222
# Total Submissions: 203725
# Difficulty: Medium
# Contributors: Admin
# Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."
# 
# For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as the h-index.


# 2017.03.12 O(n) 
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        dic = [ 0 for x in xrange(n + 1) ]
        
        for i in xrange(n):
            if citations[i] >= n:
                dic[n] += 1
            else:
                dic[citations[i]] += 1
        tot = 0
        for h in xrange(n, 0, -1):
            tot += dic[h]
            if tot >= h:
                return h
        return 0
            


# 2017.03.12 Sorted method
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        n = len(citations)
        
        for h in xrange(n, 0, -1):
            i = n - h
            if citations[i] >= h:
                return n - i
        
        return 0
