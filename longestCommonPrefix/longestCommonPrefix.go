package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	prefix := strs[0]
	for x := 1; x < len(strs); x++ {
		newPrefix := ""
		for y := 0; y < len(prefix); y++ {
			if y < len(strs[x]) && prefix[y] == strs[x][y] {
				newPrefix += string(strs[x][y])
			} else {
				break
			}
		}
		prefix = newPrefix
	}
	return prefix
}

func main() {
	fmt.Println(longestCommonPrefix([]string{"flower", "flow", "flight"}))
}
