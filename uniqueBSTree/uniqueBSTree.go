package main

import "fmt"

//Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
func numTrees(n int) int {
	//More on catalan number: https://www.geeksforgeeks.org/program-nth-catalan-number/
	//loop through n to calculate uniqueBST for each root. Since each root is different, the BST must be unique
	//g(0)=g(1)=1
	//g(n) = F(1, n) + F(2, n) + ... + F(n, n)
	//F(i, n) = g(i-1)*g(n-i), 1 <= i <= n
	//combining the formula: G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)

	gList := make([]int, n+1)
	gList[0] = 1
	gList[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j <= i; j++ {
			gList[i] += gList[j-1] * gList[i-j]
		}
	}
	return gList[n]
}

func main() {
	fmt.Println(numTrees(3))
}
