class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 2 or numRows == 1: 
            return s

        #1 Creating res[] based on zigzag rule
        res = ["" for x in range(numRows)]

        i = 0
        while i < len(s):
            j = 0
            while j < numRows and i < len(s):
                res[j] += s[i]
                i, j = i + 1, j + 1
            j = j - 2
            while j > 0 and i < len(s):
                res[j] += s[i]
                i, j = i + 1, j - 1

        #2 Getting result from res_str
        res_str = ""
        for i in range(numRows):
            res_str += res[i]

        return res_str

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("A", 1))
    print(sol.convert("A", 2))
    print(sol.convert("A", 3))
    print(sol.convert("AB", 1))
    print(sol.convert("AB", 2))
    print(sol.convert("AB", 3))
    print(sol.convert("ABCDEF", 3))
    print(sol.convert("PAYPALISHIRING", 3))
