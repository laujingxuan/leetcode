#Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#Return the maximum product you can get.
def integerBreak(n):
    return integerBreakHelper(n, 1, 0)

def integerBreakHelper(n, currentMultiplication, count):
    if (n == 1 or n == 0) and count >= 2:
        return currentMultiplication
    
    if n==0:
        return 0

    largestMultiplication = 0
    for i in range(1, n+1):
        output = integerBreakHelper(n-i, currentMultiplication * i, count+1)
        largestMultiplication = max(largestMultiplication, output)
    return largestMultiplication


def integerBreakMath(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    remainder = n%3
    numberOfThree = n//3
    if remainder == 0:
        return 3 ** numberOfThree
    if remainder == 1:
        return (3 ** (numberOfThree-1)) * 4
    else:
        return (3 ** numberOfThree) * 2

if __name__ == '__main__':
    print(integerBreak(24))
    print(integerBreakMath(24))
