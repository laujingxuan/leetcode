package main

import "fmt"

func romanToInt(s string) int {
	valueMap := map[string]int{
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000,
	}
	total := 0
	preVal := 0
	for x := len(s) - 1; x >= 0; x-- {
		if elem, ok := valueMap[string(s[x])]; ok {
			if elem >= preVal {
				total += elem
				preVal = elem
			} else {
				total -= elem
				preVal = elem
			}
		}
	}
	return total
}

func main(){
	fmt.Println(romanToInt("MCMXCIV"))
}