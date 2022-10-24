package main

import "fmt"

//can open multiple before close
func isValid(s string) bool {
    checkMap := map[rune]rune{
        '{':'}',
        '(':')',
        '[':']',
    }
    closingRunes := []rune{}
    for _,c:=range(s){
        if elem, ok:= checkMap[c]; ok{
            closingRunes = append(closingRunes, elem)
        } else if len(closingRunes) == 0 || closingRunes[len(closingRunes)-1] != c {
            return false
        }else{
			closingRunes = closingRunes[:len(closingRunes)-1]
		}
    }
	return len(closingRunes)==0
}

//must close before open a new one
func isValidAlt(s string) bool{
	checkMap := map[rune]rune{
        '{':'}',
        '(':')',
        '[':']',
    }
	for i,c := range(s){
		if elem, ok:= checkMap[c]; ok{
            if i+1<len(s) && rune(s[i+1]) == elem{
				continue
			}
			return false
        }
	}
	return true
}

func main(){
	fmt.Println(isValidAlt("()"))
}