package main

import "fmt"

func main() {
	fmt.Println(letterCombinations("23"))
	fmt.Println(letterCombinations(""))
}

// Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
// mapping is like old phone
func letterCombinations(digits string) []string {
	mapCheck := map[string][]string{
		"2": []string{"a", "b", "c"},
		"3": []string{"d", "e", "f"},
		"4": []string{"g", "h", "i"},
		"5": []string{"j", "k", "l"},
		"6": []string{"m", "n", "o"},
		"7": []string{"p", "q", "r", "s"},
		"8": []string{"t", "u", "v"},
		"9": []string{"w", "x", "y", "z"},
	}
	combinations := []string{}
	for _, digit := range digits {
		chars := mapCheck[string(digit)]
		if len(combinations) == 0 {
			for _, char := range chars {
				combinations = append(combinations, char)
			}
			continue
		}
		tempCombinations := []string{}
		for _, combination := range combinations {
			for _, char := range chars {
				temp := combination + char
				tempCombinations = append(tempCombinations, temp)
			}
		}
		combinations = tempCombinations
	}

	return combinations
}
