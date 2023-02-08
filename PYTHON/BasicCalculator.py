# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
# s consists of digits, '+', '-', '(', ')', and ' '.
class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        # 1 stands for positive, -1 stands for negative
        sign = 1
        num = 0
        index = 0
        stack = []
        while index < len(s):
            if s[index].isdigit():
                num = num*10 + int(s[index])
            if not s[index].isdigit() and s[index] != " ":
                if s[index] == "(":
                    stack.append(total)
                    stack.append(sign)
                    total = 0
                    sign = 1
                elif s[index] == ")":
                    num *= sign
                    total = (total + num) * stack.pop() + stack.pop()
                    num = 0
                else:
                    num *= sign
                    total += num
                    num = 0
                    sign = 1
                    if s[index] == "-":
                        sign = -1
            index += 1
        num *= sign
        total += num
        return total

    #slightly worse time complexity as above ideal solution is just one pass
    def calculateNonIdeal(self, s: str) -> int:
        total = 0
        sign = "+"
        num = 0
        index = 0
        while index < len(s):
            if s[index].isdigit():
                num = num*10 + int(s[index])
            if not s[index].isdigit() and s[index] != " ":
                if s[index] == "(":
                    start = index + 1
                    noOfOpen = 1
                    index += 1
                    while noOfOpen > 0:
                        if s[index] == ")":
                            noOfOpen -=1
                        if s[index] == "(":
                            noOfOpen += 1
                        # print(noOfOpen)
                        index += 1
                    # print(s[start:index - 1])
                    num = self.calculate(s[start:index - 1])
                    # print(num)
                    continue
                if sign == "+":
                    total += num
                if sign == "-":
                    total -= num
                num = 0
                sign = s[index]
            index += 1
        if sign == "-":
            total -= num
        else:
            total += num
        return total

if __name__ == "__main__":
    test = Solution()
    print(test.calculate("(1+(4+5+2)-3)+(6+8)"))
    # print(test.calculate("1-(     -2)"))
    # print(test.calculate("4+5+2"))
