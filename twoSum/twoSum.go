package main

import (
	"fmt"
	"sort"
)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
func twoSum(nums []int, target int) []int {
	for i, num := range nums {
		val := target - num
		for y, secondNum := range nums {
			if y != i && val == secondNum {
				return []int{i, y}
			}
		}

	}
	return []int{}
}

func twoSumAlt(nums []int, target int) []int {
	if len(nums) == 0 || len(nums) == 1 {
		return []int{}
	}
	sort.Ints(nums)
	start := 0
	end := len(nums) - 1
	for end > start {
		temp := nums[start] + nums[end]
		if temp == target {
			return []int{start, end}
		}
		if temp > target {
			end--
			continue
		}
		start++
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSumAlt([]int{11, 7, 2, 15}, 9))
}
