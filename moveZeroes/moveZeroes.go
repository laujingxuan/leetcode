package main

import "fmt"

func moveZeroes(nums []int) {
	if len(nums) == 0 {
		return
	}
	firstPointer := 0
	secondPointer := 0
	for i := 0; i < len(nums); i++ {
		if nums[firstPointer] == 0 && secondPointer < len(nums) {
			for secondPointer < len(nums) {
				if nums[secondPointer] != 0 {
					nums[firstPointer] = nums[secondPointer]
					nums[secondPointer] = 0
					break
				}
				secondPointer++
			}
		}
		firstPointer++
		secondPointer++
		if secondPointer >= len(nums) {
			break
		}
	}
}

func moveZeroesAlternative(nums []int) {
	if len(nums) == 0 || len(nums) == 1 {
		return
	}

	anotherPointer := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[anotherPointer] = nums[i]
			anotherPointer++
		}
	}
	for anotherPointer < len(nums) {
		nums[anotherPointer] = 0
		anotherPointer++
	}
}

func main() {
	input := []int{1, 0}
	moveZeroes(input)
	moveZeroesAlternative(input)
	fmt.Println(input)
}
