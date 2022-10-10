package main

//Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
func reverse(x int) int {
	num := x
	reverseNum := 0
	loopCount := 9 //As reverse of value >10 digits might cause overflow
	for num > 0 && loopCount > 0 {
		lastDigit := num % 10
		reverseNum = reverseNum*10 + lastDigit
		num = num / 10
		loopCount = -1
	}
	if num == 0 {
		return reverseNum
	}
	if x < 0 {

	}
}
