package helper

//Implements an algorithm to determine if a string has all unique characters (Without hashmap)
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

//Given two strings, write a method to decide if one is a permutation of the other
//A permutation is an arrangement of objects in a definite order. For example, the permutation of set A={1,6} is 2, such as {1,6}, {6,1}.
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

//Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the 'true' length of the string
func UrLify(s string, trueLength int) string {
	return ""
}
