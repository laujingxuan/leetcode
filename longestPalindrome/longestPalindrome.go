package main

import (
	"fmt"
)

// A string is called a palindrome string if the reverse of that string is the same as the original string.
func longestPalindrome(s string) string {
	longestPalin := ""
	for x := 0; x < len(s); x++ {
		oddPalindrome := expandSelf(x, x, s)
		evenPalindrome := expandSelf(x, x+1, s)
		longPalin := evenPalindrome
		if len(oddPalindrome) > len(evenPalindrome) {
			longPalin = oddPalindrome
		}
		if len(longPalin) > len(longestPalin) {
			longestPalin = longPalin
		}
	}
	return longestPalin
}

func expandSelf(leftIndex, rightIndex int, s string) string {
	temp := ""
	for leftIndex >= 0 && rightIndex < len(s) && s[leftIndex] == s[rightIndex] {
		temp = s[leftIndex : rightIndex+1]
		leftIndex -= 1
		rightIndex += 1
	}
	return temp
}

func main() {
	fmt.Println(longestPalindrome("SQQSYYSQQS"))
}
