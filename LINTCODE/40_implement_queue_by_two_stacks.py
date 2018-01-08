# 40. Implement Queue by Two Stacks 
# As the title described, you should only use two stacks to implement a queue's actions.
# 
# The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.
# 
# Both pop and top methods should return the value of first element.
# 
# Have you met this question in a real interview? Yes
# Example
# push(1)
# pop()     // return 1
# push(2)
# push(3)
# top()     // return 2
# pop()     // return 2


# 12.30.2017
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(element)
        while self.s2:
            self.s1.append(self.s2.pop())

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.s1.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.s1[-1]

