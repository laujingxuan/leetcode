package main

import "fmt"

//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
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

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
