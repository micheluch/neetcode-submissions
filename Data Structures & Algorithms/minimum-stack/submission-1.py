class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_index = -1

    def push(self, val: int) -> None:
        self.top_index += 1
        self.stack[self.top_index:] = [val]
        if self.min_stack != []:
            min_val = self.min_stack[self.top_index-1]
        else:
            min_val = float('inf')
        if val <= min_val:
            self.min_stack[self.top_index:] = [val]
        else:
            self.min_stack[self.top_index:] = [min_val]

    def pop(self) -> None:
        del self.stack[self.top_index]
        del self.min_stack[self.top_index]
        self.top_index -= 1

    def top(self) -> int:
        return self.stack[self.top_index]

    def getMin(self) -> int:
        return self.min_stack[self.top_index]     
