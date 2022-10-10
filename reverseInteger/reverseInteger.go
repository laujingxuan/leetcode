package main

import (
	"fmt"
	"math"
)

// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
func reverse(x int) int {
	reverseNum := 0
	loopCount := 9 //As reverse of value >10 digits might cause overflow
	for x != 0 && loopCount > 0 {
		lastDigit := x % 10
		reverseNum = reverseNum*10 + lastDigit
		x = x / 10
		loopCount -= 1
	}
	if x == 0 {
		return reverseNum
	}
	if reverseNum < math.MinInt32/10 || reverseNum > math.MaxInt32/10 {
		return 0
	}
	if reverseNum == math.MinInt32/10 && (x < -8 || x > 7) {
		return 0
	}
	return reverseNum*10 + x
}

func main() {
	fmt.Println(reverse(-2147483412))
}
