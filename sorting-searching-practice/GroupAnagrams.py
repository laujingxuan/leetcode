# Group anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other
def groupAnagrams(stringsList):
    checkMap = {}
    for string in stringsList:
        key = "".join(sorted(string))
        if key in checkMap:
            checkMap[key].append(string)
        else:
            checkMap[key] = [string]
    output = []
    for key in checkMap:
        output = output + checkMap[key]
    return output

def groupAnagramsWithoutSorting(stringsList):
    checkMap = {}
    for string in stringsList:
        checkList = [0] * 26
        for i in range(len(string)):
            checkList[ord(string[i]) - ord("a")] += 1
        key = "".join(map(str, checkList))
        if key in checkMap:
            checkMap[key].append(string)
        else:
            checkMap[key] = [string]
    output = []
    for key in checkMap:
        output = output + checkMap[key]
    return output       


if __name__ == "__main__":
    stringsList = ["bbb", "abc", "ccc","bac", "ba","cab","ab"]
    # print(groupAnagrams(stringsList))
    print(groupAnagramsWithoutSorting(stringsList))