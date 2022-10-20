package main

import "fmt"

//Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
//If target is not found in the array, return [-1, -1].
//You must write an algorithm with O(log n) runtime complexity.
func searchRange(nums []int, target int) []int {
	low := 0
	high := len(nums) - 1
	for high >= low {
		midIndex := (low + high) / 2
		midValue := nums[midIndex]
		if midValue < target {
			high = midIndex - 1
		}
		if midValue > target {
			low = midIndex + 1
		}
		if midValue == target {
			fmt.Println("found:", midIndex)
			return (checkTargetRange(midIndex, target, high, low, nums))
		}
	}
	return []int{-1, -1}
}

func checkTargetRange(foundIndex, target, high, low int, nums []int) []int {
	//find starting
	startLow := low
	startHigh := foundIndex - 1
	for startHigh >= startLow {
		midIndex := (startHigh + startLow) / 2
		midValue := nums[midIndex]
		if midValue == target {
			startHigh = midIndex - 1
		}
		if midValue < target {
			startLow = midIndex + 1
		}
	}
	startIndex := startLow

	//find ending
	endLow := foundIndex + 1
	endHigh := high
	for endHigh >= endLow {
		midIndex := (endLow + endHigh) / 2
		midValue := nums[midIndex]
		if midValue == target {
			endLow = midIndex + 1
		}
		if midValue > target {
			endHigh = midIndex - 1
		}
	}
	endIndex := endHigh
	return []int{startIndex, endIndex}
}

func main() {
	fmt.Println(searchRange([]int{5, 7, 7, 8, 8, 10}, 8))
}
