package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1))
}

// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
// Return the sum of the three integers.
// You may assume that each input would have exactly one solution.
func threeSumClosest(nums []int, target int) int {
	if len(nums) < 3 {
		return -1
	}
	sort.Ints(nums)
	closest := nums[0] + nums[1] + nums[2]
	for i := 0; i < len(nums)-2; i++ {
		start := i + 1
		end := len(nums) - 1
		for end > start {
			temp := nums[i] + nums[start] + nums[end]
			if math.Abs(float64(temp)-float64(target)) < math.Abs(float64(closest)-float64(target)) {
				closest = temp
			}
			if temp-target == 0 {
				return temp
			}
			if temp-target > 0 {
				end--
			} else {
				start++
			}
		}
	}
	return closest
}
