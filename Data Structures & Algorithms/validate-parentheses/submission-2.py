class Solution:
    open_b = "({["
    close_b = ")}]"

    def isValid(self, s: str) -> bool:
        result = False
        stack = []
        for b in s:
            open_indx = self.get_open(b)
            if open_indx >= 0:
                stack.append(b)
            elif len(stack) > 0:
                result = self.match_b(stack.pop(-1), b)
                if result == False: break
            else:
                result = False
                break
        if len(stack) > 0: result = False
        return result

    def match_b(self, open_b, close_b):
        open_indx = self.get_open(open_b)
        close_indx = self.get_close(close_b)
        return open_indx == close_indx
    
    def get_open(self, b):
        result = -1
        for i in range(0, len(self.open_b)):
            if b == self.open_b[i]:
                result = i
                break
        return result

    def get_close(self, b):
        result = -1
        for i in range(0, len(self.close_b)):
            if b == self.close_b[i]:
                result = i
                break
        return result