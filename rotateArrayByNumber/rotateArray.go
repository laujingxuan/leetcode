package main

import "fmt"

func rotate(nums []int, k int) {
	for k >= len(nums) {
		k -= len(nums)
	}
	firstPointer := 0
	secondPointer := k
	tempStore := []int{}
	for i := k; i > 0; i-- {
		if secondPointer >= len(nums) {
			secondPointer = 0
		}
		tempStore = append(tempStore, nums[secondPointer])
		nums[secondPointer] = nums[firstPointer]
		firstPointer++
		secondPointer++
	}
	for i := len(nums) - k; i > 0; i-- {
		if secondPointer >= len(nums) {
			secondPointer = 0
		}
		tempStore = append(tempStore, nums[secondPointer])
		nums[secondPointer] = tempStore[0]
		tempStore = tempStore[1:]
		secondPointer++
	}
}

func rotateWithSpaceOne(nums []int, k int) {
	k = k % len(nums)
	//rotate the whole array first
	reverseArray(nums, 0, len(nums)-1)
	//reverse the first k elements in the array
	reverseArray(nums, 0, k-1)
	//reverse the elements after kth element
	reverseArray(nums, k, len(nums)-1)
}

func reverseArray(nums []int, startingInd, endingInd int) {
	for endingInd > startingInd {
		temp := nums[startingInd]
		nums[startingInd] = nums[endingInd]
		nums[endingInd] = temp
		startingInd++
		endingInd--
	}
}

func main() {
	nums := []int{-1}
	//rotate(nums, 2)
	rotateWithSpaceOne(nums, 2)
	fmt.Println(nums)
}
