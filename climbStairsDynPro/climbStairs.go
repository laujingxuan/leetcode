package main

func climbStairs(n int) int {
	cacheArray := make([]int, n)
	return finoIdea(n, cacheArray)
}

func finoIdea(n int, cacheArray []int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else if n == 2 {
		return 2
	}

	if cacheArray[n-1] == 0 {
		cacheArray[n-1] = finoIdea(n-1, cacheArray) + finoIdea(n-2, cacheArray)
	}

	return cacheArray[n-1]
}
