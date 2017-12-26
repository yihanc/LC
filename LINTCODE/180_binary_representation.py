
# It seems that test cases doesn't include negative case
class Solution:
    """
    @param: n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binaryRepresentation(self, n):
        # write your code here
        if "." not in n:
            return self.parseInt(n)
        intg, frac = n.split(".")
        #print(intg, frac)        
        b_frac = self.parseFrac(frac)
        if b_frac == "ERROR": return b_frac
        b_intg = self.parseInt(intg)
        #print(b_intg, b_frac)
        return b_intg + "." + b_frac if b_frac else b_intg
    
    def parseInt(self, s):
        if not s or s == "" or s == "0" or s == "-0": return "0"
        return bin(((1 << 32) - 1) & int(s))[2:]

    def parseFrac(self, s):
        f = float("0." + s)
        dic = {}
        res = ""
        while f:
            print(dic)
            if len(res) > 32 or f in dic:
                return "ERROR"
            dic[f] = True
            f = f * 2
            if f >= 1:
                res += "1"
                f -= 1
            else:
                res += "0"
        return res
        
        
