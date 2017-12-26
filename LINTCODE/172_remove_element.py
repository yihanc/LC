# 172. Remove Element 
# 
#  Description
#  Notes
#  Testcase
#  Judge
# Given an array and a value, remove all occurrences of that value in place and return the new length.
# 
# The order of elements can be changed, and the elements after the new length don't matter.
# 
# Have you met this question in a real interview? Yes
# Example
# Given an array [0,4,4,0,0,2,4,4], value=4
# 
# return 4 and front four elements of the array is [0,0,0,2]
# 

# Mon Dec 11 12:43:42 EST 2017
# If not in place, ```return filter(lambda x: x != elem, A)```

# Inplace
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        A[:] = [i for i in A if i != elem]
        return len(A)



