package main

import (
	"fmt"
	"math"
)

func sortedSquares(nums []int) []int {
	negativeNums := []int{}
	sortedSqNums := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i] < 0 {
			negativeNums = append(negativeNums, nums[i])
			continue
		}

		positiveNumSq := nums[i] * nums[i]
		if len(negativeNums) != 0 {
			smallestNegativeNumSq := negativeNums[len(negativeNums)-1] * negativeNums[len(negativeNums)-1]
			if positiveNumSq > smallestNegativeNumSq {
				sortedSqNums = append(sortedSqNums, smallestNegativeNumSq)
				negativeNums = negativeNums[:len(negativeNums)-1]
				i--
				continue
			}
		}
		sortedSqNums = append(sortedSqNums, positiveNumSq)

	}
	if len(negativeNums) != 0 {
		for i := len(negativeNums) - 1; i >= 0; i-- {
			sortedSqNums = append(sortedSqNums, negativeNums[i]*negativeNums[i])
		}
	}
	return sortedSqNums
}

func sortedSquaresTwoPointers(nums []int) []int {
	sortedSquareNums := make([]int, len(nums))
	frontIndex := 0
	lastIndex := len(nums) - 1
	for i := lastIndex; i >= 0; i-- {
		if math.Abs(float64(nums[lastIndex])) > math.Abs(float64(nums[frontIndex])) {
			sortedSquareNums[i] = nums[lastIndex] * nums[lastIndex]
			lastIndex--
			continue
		}
		sortedSquareNums[i] = nums[frontIndex] * nums[frontIndex]
		frontIndex++
	}
	return sortedSquareNums
}

func main() {
	fmt.Println(sortedSquares([]int{-7, -3, 2, 3, 11}))
	fmt.Println(sortedSquares([]int{-1}))
	fmt.Println(sortedSquaresTwoPointers([]int{-7, -3, 2, 3, 11}))
	fmt.Println(sortedSquaresTwoPointers([]int{-1}))
}
