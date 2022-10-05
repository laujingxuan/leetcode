package helper

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// Implements an algorithm to determine if a string has all unique characters (Without hashmap)
func IsUnique(input string) bool {
	//only 128 chars in AsCii
	boolArray := make([]bool, 128)
	for x := 0; x < len(input); x++ {
		if boolArray[input[x]] {
			return false
		}
		boolArray[input[x]] = true
	}
	return true
}

// Given two strings, write a method to decide if one is a permutation of the other
// A permutation is an arrangement of objects in a definite order. For example, the permutation of set A={1,6} is 2, such as {1,6}, {6,1}.
func CheckPermutation(a, b string) bool {
	//alternate implementation without hashmap
	//1) sort the stings and compare
	//2) create a list of length 128 to store the char instead (assume ASCii)
	mapA := make(map[rune]int)
	mapB := make(map[rune]int)
	for _, char := range a {
		number := mapA[char]
		number += 1
		mapA[char] = number
	}
	for _, char := range b {
		number := mapB[char]
		number += 1
		mapB[char] = number
	}
	if len(mapA) != len(mapB) {
		return false
	}
	for k, v := range mapA {
		if v != mapB[k] {
			return false
		}
		delete(mapB, k)
	}
	return len(mapB) == 0
}

// Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the 'true' length of the string
func UrLify(s string, trueLength int) string {
	var sb strings.Builder
	for x := 0; x < trueLength; x++ {
		if string(s[x]) == " " {
			sb.WriteString("%20")
		} else {
			sb.WriteString(string(s[x]))
		}
	}
	return sb.String()
}

// Is the string a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters
func IsPalindromePermutation(s string) bool {
	charList := make([]int, 128)
	numOfOdd := 0
	for x := 0; x < len(s); x++ {
		charList[s[x]-1] = charList[s[x]-1] + 1
		if charList[s[x]-1]%2 != 0 {
			numOfOdd += 1
		} else {
			numOfOdd -= 1
		}
	}

	return numOfOdd <= 1
}

// There are three types of edits that can be performed on strinsg: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away
func IsOneAway(s, p string) bool {
	if len(s) == len(p) {
		diffCount := 0
		for x := 0; x < len(s); x++ {
			if s[x] != p[x] {
				diffCount += 1
			}
			if diffCount > 1 {
				return false
			}
		}
		return true
	}
	//another way is to keep track of the index and compare. Like if unmatch, then move longer string index + 1. Else, move both string index + 1
	if math.Abs(float64(len(s)-len(p))) == 1 {
		shorter := p
		if len(s) < len(p) {
			shorter = s
		}
		sBehind := s
		pBehind := p
		for x := 0; x < len(shorter); x++ {
			if s[x] != p[x] {
				sBehind = s[x:]
				pBehind = p[x:]
				break
			}
		}
		if len(sBehind) > len(pBehind) {
			return sBehind[1:] == pBehind
		} else {
			return pBehind[1:] == sBehind
		}
	}
	return false
}

// A method to perform basic string compression using the counts of repeated characters. For example. the string aabcccccaaa would become a2b1c5a3
func StringCompression(s string) string {
	if len(s) <= 1 {
		return s
	}
	var sb strings.Builder
	trackCount := 0
	for x := 0; x < len(s)-1; x++ {
		trackCount += 1
		if s[x] != s[x+1] {
			sb.WriteString(string(s[x]) + strconv.Itoa(trackCount))
			trackCount = 0
		}
	}
	if trackCount != 0 {
		sb.WriteString(string(s[len(s)-1]) + strconv.Itoa(trackCount))
	}
	compressedString := sb.String()
	if len(compressedString) > len(s) {
		return s
	}

	return compressedString
}

// Rotate the matrix by 90 degrees
func RotateMatrix(matrix [][]int) {
	fmt.Println(matrix)
	for i := 0; i < len(matrix); i++ {
		lastInd := len(matrix) - i - 1
		for y := i; y < lastInd; y++ {
			offset := y - i
			temp := matrix[i][y]
			matrix[i][y] = matrix[lastInd-offset][i]
			matrix[lastInd-offset][i] = matrix[lastInd][lastInd-offset]
			matrix[lastInd][lastInd-offset] = matrix[y][lastInd]
			matrix[y][lastInd] = temp
		}
	}
}
