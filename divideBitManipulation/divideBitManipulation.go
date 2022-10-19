package main

import (
	"fmt"
	"math"
)

//Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
// The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
//Return the quotient after dividing dividend by divisor.
func divide(dividend int, divisor int) int {

	if dividend == math.MinInt32 && divisor == -1 {
		return math.MaxInt32
	}

	isNegative := (dividend ^ divisor) < 0
	dividend = int(math.Abs(float64(dividend)))
	divisor = int(math.Abs(float64(divisor)))
	//dividend = quotient * divisor + remainder
	quotient := 0
	for dividend-divisor >= 0 {
		tempStart := 0
		for dividend-(divisor<<(tempStart+1)) >= 0 {
			tempStart++
		}
		quotient += 1 << tempStart
		dividend -= divisor << tempStart
	}

	if isNegative {
		return -quotient
	}
	return quotient
}

func main() {
	fmt.Println(divide(10, 3))
}
