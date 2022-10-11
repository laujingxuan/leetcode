package main

import "fmt"

func maxArea(height []int) int {
	if len(height) < 2 {
		return 0
	}
	firstPointer := 0
	lastPointer := len(height) - 1
	maximumA := 0
	for lastPointer > firstPointer {
		if height[firstPointer] > height[lastPointer] {
			tempArea := height[lastPointer] * (lastPointer - firstPointer)
			if tempArea > maximumA {
				maximumA = tempArea
			}
			lastPointer -= 1
		} else {
			tempArea := height[firstPointer] * (lastPointer - firstPointer)
			if tempArea > maximumA {
				maximumA = tempArea
			}
			firstPointer += 1
		}
	}
	return maximumA
}

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
	fmt.Println(maxArea([]int{1, 1}))
}
