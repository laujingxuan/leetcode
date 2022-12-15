class Solution:
    def asteroidCollision(self, asteroids):
        i = 0
        stack = []
        while i < len(asteroids):
            print(asteroids[i])
            print("i:" + str(i))
            if len(stack) == 0 or not (stack[-1] > 0 and asteroids[i] < 0):
                print("before:" + str(stack))
                stack.append(asteroids[i])
                print("after:" + str(stack))
                i += 1
                continue
            while True:
                if len(stack) == 0 or not (stack[-1] > 0 and asteroids[i] < 0):
                    stack.append(asteroids[i])
                    break
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    break
                elif abs(stack[-1])< abs(asteroids[i]):
                    stack.pop()
                    continue
                else:
                    break
            i += 1
        return stack

if __name__ == "__main__":
    test = Solution()
    # print(test.asteroidCollision([5,10,-5]))
    print(test.asteroidCollision([-2,1,-1,-2]))