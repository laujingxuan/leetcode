package helper

//Implements an algorithm to determine if a string has all unique characters (Without hashmap)
func IsUnique(input string) bool {
	//only 128 chars in AsCii
	boolArray := make([]bool, 128)
	for x := 0; x < len(input); x++ {
		if boolArray[input[x]] {
			return false
		}
		boolArray[input[x]] = true
	}
	return true
}
