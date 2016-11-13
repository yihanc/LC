# 371. Sum of Two Integers   QuestionEditorial Solution  My Submissions
# Total Accepted: 44827
# Total Submissions: 86931
# Difficulty: Easy
# Contributors: Admin
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
# 
# Example:
# Given a = 1 and b = 2, return 3.
# 
# Credits:
# pecial thanks to @fujiaozhu for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            print( "---------------")
            # ^ get different bits and & gets double 1s, << moves carry
            print("a, b, a&b        : " + bin(a) + " " + bin(b) + " " + bin(a&b)) 
            carry = a & b
            print("a^b, a^b&mask    : " + bin(a^b) + " " + bin((a^b)&mask))
            a = (a ^ b) & mask
            print("carry            : " + bin(carry<<1) + " " + bin((carry<<1) & mask))
            b = (carry << 1) & mask

        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        print("~(a ^ mask)      : " + bin(~(a^mask)))
        
        return a if a <= MAX else ~(a ^ mask)

if __name__ == "__main__":
    Solution().getSum(-12, -8)


exit

# Java
# public class Solution {
#     public int getSum(int a, int b) {
#         while (b != 0) {
#             int carry = a & b;
#             a = a ^ b;
#             b = (carry << 1);
#         }
#         return a;
#     }
# }
