package main

import (
	"fmt"
)

// Given a string s, find the length of the longest substring without repeating characters.
func lengthOfLongestSubstring(s string) int {
	currentSubstring := ""
	finalSubstring := ""
	addedMap := map[string]int{}
	for x := 0; x < len(s); x++ {
		valid := false
		position, ok := addedMap[string(s[x])]
		if len(currentSubstring) != 0 && position >= addedMap[string(currentSubstring[0])] {
			valid = true
		}
		if ok && valid {
			if len(currentSubstring) > len(finalSubstring) {
				finalSubstring = currentSubstring
			}
			currentSubstring = s[position+1 : x]
		}
		addedMap[string(s[x])] = x
		currentSubstring += string(s[x])
		if x == len(s)-1 {
			if len(currentSubstring) > len(finalSubstring) {
				return len(currentSubstring)
			}
		}
	}
	return len(finalSubstring)
}

func betterLengthOfLongestSubstring(s string) int {
	longest := 0
	startIndex := 0
	addedMap := map[string]int{}
	for index, val := range s {
		if foundIndex, ok := addedMap[string(val)]; ok {
			if foundIndex+1 > startIndex {
				startIndex = foundIndex + 1
			}
		}
		if index-startIndex+1 > longest {
			longest = index - startIndex + 1
		}
		addedMap[string(val)] = index
	}
	return longest
}

func main() {
	fmt.Println(lengthOfLongestSubstring("kdgjkjhglfp"))
	fmt.Println(betterLengthOfLongestSubstring("kdgjkjhglfp"))
}
