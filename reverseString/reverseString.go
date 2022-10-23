package main

import "fmt"

func reverseWords(s string) string {
    runes := []rune(s)
    whiteSpacePointer := 1
    firstPointer := 0
    for whiteSpacePointer < len(s){
        if runes[whiteSpacePointer] == ' ' || whiteSpacePointer==len(runes)-1{
            reversePointer := whiteSpacePointer
            if runes[whiteSpacePointer] == ' '{
                reversePointer = whiteSpacePointer-1
            }
            for reversePointer > firstPointer {
                temp:=runes[firstPointer]
                runes[firstPointer] = runes[reversePointer]
                runes[reversePointer]= temp
                reversePointer --
                firstPointer ++
            }
            firstPointer = whiteSpacePointer+1
        }
        whiteSpacePointer ++
    }
    return string(runes)
}

func main(){
	input := "Let's take LeetCode contest"
	reverse := reverseWords(input)
	fmt.Println(reverse)
}