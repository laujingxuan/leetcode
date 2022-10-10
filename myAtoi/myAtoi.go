package main

import (
	"fmt"
	"math"
	"strings"
)

//Read in and ignore any leading whitespace.
//Check if the next character (if not already at the end of the string) is '-' or '+'
//Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
var (
	intMap = map[string]int32{
		"0": 0,
		"1": 1,
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
	}
)

func myAtoi(s string) int32 {
	trimmed := strings.TrimSpace(s)
	if len(trimmed) == 0 {
		return 0
	}
	var sign int32 = 1
	if string(trimmed[0]) == "-" || string(trimmed[0]) == "+" {
		if string(trimmed[0]) == "-" {
			sign = -1
		}
		trimmed = trimmed[1:]
	}
	var stringBuilder strings.Builder
	leadingZero := true
	for _, char := range trimmed {
		if _, ok := intMap[string(char)]; !ok {
			break
		}
		if string(char) == "0" {
			if leadingZero {
				continue
			}
		} else {
			leadingZero = false
		}
		stringBuilder.WriteString(string(char))

	}
	digitString := stringBuilder.String()
	if len(digitString) > 10 {
		if sign == 1 {
			return math.MaxInt32
		}
		return math.MinInt32
	}
	if len(digitString) == 10 {
		var firstNineNumber int32 = 0
		lastNumber := intMap[string(digitString[len(digitString)-1])]
		for x := 0; x < len(digitString)-1; x++ {
			digit, _ := intMap[string(digitString[x])]
			firstNineNumber = firstNineNumber*10 + digit
		}
		if firstNineNumber > math.MaxInt32/10 {
			if sign == 1 {
				return math.MaxInt32
			}
			return math.MinInt32
		}
		if firstNineNumber == math.MaxInt32/10 {
			if sign == 1 && lastNumber > 7 {
				return math.MaxInt32
			}
			if sign == -1 && lastNumber > 8 {
				return math.MinInt32
			}
		}
		return (firstNineNumber*10 + lastNumber) * sign
	}
	var total int32 = 0
	for _, char := range digitString {
		digit, _ := intMap[string(char)]
		total = total*10 + digit
	}
	return total * sign
}

func main() {
	fmt.Println(myAtoi("-435645458ABCSDsdf"))
}
