package main

import (
	"fmt"
	helper "learn/string/helper"
)

func main() {
	// fmt.Println(helper.IsUnique("abcda"))
	// fmt.Println(helper.CheckPermutation("abcd", "db"))
	// fmt.Println(helper.UrLify(" Mr John Smith    ", 15))
	// fmt.Println(helper.IsPalindromePermutation("tactcoa"))
	// fmt.Println(helper.IsOneAway("bale", "bale"))
	// fmt.Println(helper.StringCompression("aabcccccaaa"))
	input := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	helper.RotateMatrix(input)
	fmt.Println(input)
}
