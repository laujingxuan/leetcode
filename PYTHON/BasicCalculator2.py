class Solution:
    def calculateTidier(self, s):
        stack = []
        i = 0
        num = 0
        sign = "+"
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or (i == len(s) - 1):
                if sign == "+":
                    stack.append(num)
                    # print("+" + str(num))
                elif sign == "-":
                    stack.append(-num)
                    # print("-" + str(num))
                elif sign == "*":
                    stack.append(num * stack.pop())
                    # print("*" + str(num))
                elif sign == "/":
                    temp = stack.pop()
                    if temp < 0 and temp%num != 0:
                        stack.append((temp//num) + 1)
                    else:
                        stack.append(temp//num)
                num = 0
                sign = s[i]
                # print(sign)
            i += 1
        output = 0
        while len(stack) > 0:
            output += stack.pop()
        return output

    def calculateDirty(self, s):
        stack = []
        i = 0
        # handle multiplication and division
        while i < len(s):
            i = self.removeSpace(s, i)
            if i == len(s):
                break
            operator = ''
            # identify if it's a operator and what type of operator is it
            if not s[i].isdigit():
                if s[i] == '+' or s[i] == '-':
                    stack.append(s[i])
                    i += 1
                    continue
                else:
                    operator = s[i]
                    i += 1
            toAddNumber = 0
            i = self.removeSpace(s, i)
            while i < len(s) and s[i].isdigit():
                toAddNumber = toAddNumber * 10 + int(s[i])
                i += 1
            i = self.removeSpace(s, i)
            if operator != '':
                previousNumber = stack.pop()
                if operator == '*':
                    toAddNumber = previousNumber * toAddNumber
                else:
                    toAddNumber = previousNumber // toAddNumber
            stack.append(toAddNumber)
        # handle addition and substraction
        output = stack[0]
        i = 1
        while i < len(stack):
            operator = stack[i]
            if operator == '+':
                output += stack[i + 1]
            else:
                output -= stack[i + 1]
            i += 2
        return output

    def removeSpace(self, s, currentIndex):
        while currentIndex < len(s) and s[currentIndex].isspace():
            currentIndex += 1
        return currentIndex

if __name__ == "__main__":
    test = Solution()
    # print(test.calculateTidier("3+2*2"))
    # print(test.calculateTidier("3/2"))
    print(test.calculateTidier("14-3/2"))