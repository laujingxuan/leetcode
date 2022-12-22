# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).

class Solution:
    #O(N^2) space complexity and O(N^2log(N)) time complexity for sorting a 2D matrix (N is length of matrix)
    def kthSmallestBruteForce(self, matrix, k):
        allElements = []
        for i in range(len(matrix)):
            allElements += matrix[i]
        allElements.sort()
        return allElements[k-1]
    
    # Proposed solutions are solution using heap or binary search. Way too complicated i think. Can refer to 378. Kth Smallest Element in a Sorted Matrix solution
