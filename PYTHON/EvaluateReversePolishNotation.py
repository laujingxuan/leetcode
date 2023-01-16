class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if self.isdigit(token):
                stack.append(int(token))
            else:
                secondValue = stack.pop()
                firstValue = stack.pop()
                newValue = 0
                if token == "+":
                    newValue = firstValue + secondValue
                elif token == "-":
                    newValue = firstValue - secondValue
                elif token == "*":
                    newValue = firstValue * secondValue
                else:
                    newValue = int(firstValue/secondValue)
                stack.append(newValue)
        return stack.pop()

    def isdigit(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False