#Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
#Return the maximum product you can get.
def integerBreak(n):
    memo = [0] * (n+1)
    return integerBreakHelper(n, memo, 1, 0)

def integerBreakHelper(n, memo, currentMultiplication, count):
    if (n == 1 or n == 0) and count >= 2:
        return currentMultiplication
    
    if n==0:
        return 0

    # if memo[n] != 0:
    #     return memo[n]

    largestMultiplication = 0
    for i in range(1, n+1):
        # if i == 2 and n == 4:
        #     print("i:" + str(i))
        #     print(currentMultiplication)
        #     print(count)
        #     print("n-i: " + str(n-i))
        output = integerBreakHelper(n-i, memo, currentMultiplication * i, count+1)
        largestMultiplication = max(largestMultiplication, output)
    memo[n] = largestMultiplication
    # print(memo)
    return memo[n]

if __name__ == '__main__':
    print(integerBreak(10))
