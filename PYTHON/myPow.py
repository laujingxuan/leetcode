class Solution:
    #logN time complexity. Much better than looping x one by one
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        print(n)
        if n%2 == 0:
            return self.myPow(x*x, n//2)
        return x*self.myPow(x*x, n//2)