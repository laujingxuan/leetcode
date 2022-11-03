package main

import (
	"fmt"
	"strings"
)

func permute(nums []int) [][]int {
	output := [][]int{}
	return findPermutation(output, []int{}, nums)
}

func findPermutation(found [][]int, currentCombi, nums []int) [][]int {
	if len(nums) == 0 {
		return append(found, currentCombi)
	}

	for index, num := range nums {
		newNums := make([]int, len(nums))
		copy(newNums, nums)
		newNums[index] = newNums[len(newNums)-1]
		newNums = newNums[:len(newNums)-1]
		found = findPermutation(found, append(currentCombi, num), newNums)
	}
	return found
}

func main() {
	// fmt.Println(permute([]int{1, 2, 3}))
	fmt.Println(letterCasePermutationBFS("3z4"))
}

func letterCasePermutation(s string) []string {
	output := []string{}
	input := []rune(s)
	return backTrack(output, "", input)
}

func backTrack(output []string, temp string, input []rune) []string {
	if len(temp) == len(input) {
		return append(output, temp)
	}

	index := len(temp)
	if (input[index] < 'a' || input[index] > 'z') && (input[index] < 'A' || input[index] > 'Z') {
		output = backTrack(output, temp+string(input[index]), input)
		return output
	}
	output = backTrack(output, temp+strings.ToLower(string(input[index])), input)
	output = backTrack(output, temp+strings.ToUpper(string(input[index])), input)
	return output
}

func letterCasePermutationBFS(s string) []string {
	if len(s) == 0 {
		return []string{}
	}

	queue := []string{}
	queue = append(queue, s)

	for j := 0; j < len(s); j++ {
		qLen := len(queue)
		for i := 0; i < qLen; i++ {
			currentString := queue[0]
			queue = queue[1:]
			currentRune := rune(currentString[j])
			if (currentRune < 'a' || currentRune > 'z') && (currentRune < 'A' || currentRune > 'Z') {
				queue = append(queue, currentString)
				continue
			}
			currentString = currentString[:j] + strings.ToLower(string(currentString[j])) + currentString[j+1:]
			queue = append(queue, currentString)
			currentString = currentString[:j] + strings.ToUpper(string(currentString[j])) + currentString[j+1:]
			queue = append(queue, currentString)
		}
	}

	return queue
}
