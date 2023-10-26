class MinStack:

    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        currMin = self.getMin()
        if currMin == None or currMin > val:
            currMin = val
        self.stack.append([val, currMin])
        

    def pop(self) -> None:
        if self.stack:
            poped = self.stack.pop()
            return poped[0]
        else:
            return "undefined"
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return "undefined"
        

    def getMin(self) -> int:
        if self.stack == []:
            return None
        else:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()