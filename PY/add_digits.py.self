class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            if num < 10:
                return num
            result = 0
            for i in str(num):
                result += int(i) 
            num = result
