package main

import (
	"fmt"
)

// There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

// Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

// The test cases are generated so that the answer will be less than or equal to 2 * 109.

func main() {
	// fmt.Println(uniquePathsDFSOnly(17, 17))
	fmt.Println(uniquePathsWithDynProg(20, 20))
}

func uniquePathsWithDynProg(m int, n int) int {
	memo := make([][]int, m)
	for index, _ := range memo {
		memo[index] = make([]int, n)
	}
	uniquePathsDynHelper(m, n, m-1, n-1, memo)
	return memo[m-1][n-1]
}

func uniquePathsDynHelper(m, n, currentM, currentN int, memo [][]int) int {
	if currentM == 0 || currentN == 0 {
		memo[currentM][currentN] = 1
	}

	if currentM < 0 || currentN < 0 {
		return 0
	}
	if memo[currentM][currentN] != 0 {
		return memo[currentM][currentN]
	}
	memo[currentM][currentN] = uniquePathsDynHelper(m, n, currentM-1, currentN, memo) + uniquePathsDynHelper(m, n, currentM, currentN-1, memo)

	return memo[currentM][currentN]
}

func uniquePathsDFSOnly(m int, n int) int {
	return uniquePathsDFSHelper(m, n, 0, 0)
}

func uniquePathsDFSHelper(m, n, currentM, currentN int) int {
	if currentM >= m || currentN >= n {
		return 0
	}
	if currentM == m-1 && currentN == n-1 {
		return 1
	}
	mTotal := 0
	nTotal := 0
	if currentM < m-1 {
		mTotal = uniquePathsDFSHelper(m, n, currentM+1, currentN)
	}
	if currentN < n-1 {
		nTotal = uniquePathsDFSHelper(m, n, currentM, currentN+1)
	}
	return mTotal + nTotal
}

// public int uniquePathsRecursiveWay(int m, int n) {
//     int[][] grid = new int[n][m];

//     for (int i = 0; i < n; i++) {
//       for (int j = 0; j < m; j++) {
//         if (i == 0) grid[0][j] = 1;
//         if (j == 0) grid[i][j] = 1;
//         if (i != 0 && j != 0) {
//           int up = grid[i - 1][j];
//           int left = grid[i][j - 1];
//           grid[i][j] = up + left;
//         }
//       }
//     }
//     return grid[n - 1][m - 1];
//   }
