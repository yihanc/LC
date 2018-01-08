# 2017.12.30

class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.s1.append(number)
        if not self.s2 or number < self.s2[-1]:
            self.s2.append(number)
        else:
            self.s2.append(self.s2[-1])
        

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.s2.pop()
        return self.s1.pop()

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if self.s2:
            return self.s2[-1]
        else:
            raise Exception("Stack is empty!")

