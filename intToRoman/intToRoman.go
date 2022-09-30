package main

import "fmt"

func intToRoman(num int) string {
	minusMap := map[int]string{
		1:    "I",
		5:    "V",
		10:   "X",
		50:   "L",
		100:  "C",
		500:  "D",
		1000: "M",
	}
	intList := []int{1, 5, 10, 50, 100, 500, 1000}
	romanString := ""
	for x := len(intList) - 1; x >= 0; x-- {
		for num-intList[x] >= 0 {
			num -= intList[x]
			romanString += minusMap[intList[x]]
		}
		firstDigit := intList[x]
		for firstDigit >= 10 {
			firstDigit = firstDigit / 10
		}
		var toAddNumber int
		if firstDigit == 1 {
			toAddNumber = intList[x] / 10
		} else {
			toAddNumber = intList[x] * 2 / 10
		}
		if num+toAddNumber-intList[x] >= 0 {
			num += toAddNumber - intList[x]
			romanString += minusMap[toAddNumber]
			romanString += minusMap[intList[x]]
		}
	}
	return romanString
}

func main() {
	fmt.Println(intToRoman(1994))
}
