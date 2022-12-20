class Solution:
    def countPrimes(self, n):
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                j = 2
                while i*j < n:
                    not_prime[i*j] = True
                    j += 1
        #print not_prime
        return count