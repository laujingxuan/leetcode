package main

import (
	"fmt"
	"math"
)

func main() {
	// test := []int{7, 6, 4, 3, 1}
	// fmt.Println(maxProfit(test))
	test2 := []int{3, 2, 6, 5, 0, 3}
	fmt.Println(maxProfit(test2))
}

func maxProfit(prices []int) int {
	min := math.MaxInt
	max := math.MinInt
	currentMaxDifference := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i+1] > prices[i] {
			if prices[i] < min {
				min = prices[i]
				max = 0
			}
			if prices[i+1] > max {
				max = prices[i+1]
			}
			if min != math.MaxInt && max-min > currentMaxDifference {
				currentMaxDifference = max - min
			}
		}
	}
	if min != math.MaxInt {
		return currentMaxDifference
	}
	return 0
}

func maxProfitBetter(prices []int) int {
	min := math.MaxInt
	currentMaxDifference := 0
	for i := 0; i < len(prices)-1; i++ {
		if prices[i] < min {
			min = prices[i]
		}
		currentDifference := prices[i+1] - min
		if currentDifference > currentMaxDifference {
			currentMaxDifference = currentDifference
		}
	}
	if min != math.MaxInt {
		return currentMaxDifference
	}
	return 0
}

func maxProfitAlternate(prices []int) int {
	maxCurr := 0
	maxSoFar := 0
	for i := 0; i < len(prices)-1; i++ {
		maxCurr = int(math.Max(0, float64(maxCurr+prices[i+1]-prices[i])))
		maxSoFar = int(math.Max(float64(maxCurr), float64(maxSoFar)))
	}
	return maxSoFar
}
