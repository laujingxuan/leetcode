package main

import (
	"fmt"
	"strconv"
)

//An integer is a palindrome when it reads the same backward as forward.
func isPalindrome(x int) bool {
	stringForm := strconv.Itoa(x)
	for len(stringForm) > 0 {
		if len(stringForm) == 1 {
			return true
		}
		if stringForm[0] != stringForm[len(stringForm)-1] {
			return false
		}
		if len(stringForm) == 2 {
			return true
		}
		stringForm = stringForm[1 : len(stringForm)-1]
	}
	return true
}

func altIsPalindrome(x int) bool {
	revNumber := 0
	y := x
	for y > 0 {
		digit := y % 10
		revNumber = revNumber*10 + digit
		y = y / 10
	}

	return x == revNumber
}

func main() {
	fmt.Println(altIsPalindrome(12112))
}
