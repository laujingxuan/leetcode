package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}
	sort.Ints(nums)
	returnMatrix := [][]int{}
	checkMap := map[[3]int]bool{}
	for i := 0; i < len(nums)-2; i++ {
		firstPointer := i + 1
		secondPointer := len(nums) - 1
		for secondPointer > firstPointer {
			total := nums[i] + nums[firstPointer] + nums[secondPointer]
			if total == 0 {
				if _, ok := checkMap[[3]int{nums[i], nums[firstPointer], nums[secondPointer]}]; !ok {
					checkMap[[3]int{nums[i], nums[firstPointer], nums[secondPointer]}] = true
					returnMatrix = append(returnMatrix, []int{nums[i], nums[firstPointer], nums[secondPointer]})
				}
			}
			if total > 0 {
				secondPointer -= 1
			} else {
				firstPointer += 1
			}
		}
	}

	return returnMatrix
}

func main() {
	// fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
	// fmt.Println(threeSum([]int{0, 0, 0, 0}))
	// fmt.Println(threeSum([]int{0, 0, 1}))
	fmt.Println(threeSum([]int{-2, 0, 1, 1, 2}))
}
