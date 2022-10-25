package main

import "fmt"

func main() {
	fmt.Println(checkInclusion("hello", "ooolleoooleh"))
	fmt.Println(checkInclusionBetter("hello", "ooolleoooleh"))
	fmt.Println(checkInclusion("ab", "eidbaooo"))
	fmt.Println(checkInclusionBetter("ab", "eidbaooo"))
}

//potential nm time-complexity since we will need to repeatedly check isPermutation when char matches
func checkInclusion(s1 string, s2 string) bool {
	//add s1 to a map first by breaking number of chars of each alphabet
	s1Map := map[byte]int{}
	for i := 0; i < len(s1); i++ {
		if count, ok := s1Map[s1[i]]; ok {
			s1Map[s1[i]] = count + 1
		} else {
			s1Map[s1[i]] = 1
		}
	}
	startingIndex := 0
	lenOfS1 := len(s1)
	for startingIndex < len(s2)-len(s1)+1 {
		if _, ok := s1Map[s2[startingIndex]]; ok {
			if isPermutation(s2[startingIndex:startingIndex+lenOfS1], s1Map) {
				return true
			}
		}
		startingIndex++
	}
	return false
}

func isPermutation(s2 string, s1Map map[byte]int) bool {
	s2Map := map[byte]int{}
	for i := 0; i < len(s2); i++ {
		if count, ok := s2Map[s2[i]]; ok {
			s2Map[s2[i]] = count + 1
		} else {
			s2Map[s2[i]] = 1
		}
	}
	if len(s2Map) != len(s1Map) {
		return false
	}

	for k1, v1 := range s1Map {
		if v2, ok := s2Map[k1]; !ok || v2 != v1 {
			return false
		}
	}
	return true
}

//time complexity of length of s2 + s1 only. Since s2 > s1, time complexity is length of s2
//sliding window method
func checkInclusionBetter(s1 string, s2 string) bool {
	checkMap := map[byte]int{}
	for i := 0; i < len(s1); i++ {
		if count, ok := checkMap[s1[i]]; ok {
			checkMap[s1[i]] = count + 1
		} else {
			checkMap[s1[i]] = 1
		}
	}

	startingIndex := 0
	endIndex := 0
	for endIndex < len(s2) {
		if endIndex-startingIndex < len(s1) {
			addToWindow(checkMap, s2[endIndex])
			endIndex++
		} else {
			addToWindow(checkMap, s2[endIndex])
			removeFromWindow(checkMap, s2[startingIndex])
			startingIndex++
			endIndex++
		}
		if len(checkMap) == 0 {
			return true
		}
	}
	return false
}

func removeFromWindow(checkMap map[byte]int, key byte) {
	if count, ok := checkMap[key]; ok {
		count = count + 1
		if count == 0 {
			delete(checkMap, key)
		} else {
			checkMap[key] = count
		}
	} else {
		checkMap[key] = 1
	}
}

func addToWindow(checkMap map[byte]int, key byte) {
	if count, ok := checkMap[key]; ok {
		count = count - 1
		if count == 0 {
			delete(checkMap, key)
		} else {
			checkMap[key] = count
		}
	} else {
		checkMap[key] = -1
	}
}
