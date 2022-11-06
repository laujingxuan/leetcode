package leetcode;

import java.util.ArrayList;
import java.util.List;

public class FirstOccurInAString {
    public int strStr(String haystack, String needle) {
        if (haystack.length()==0 || needle.length()==0 || needle.length()>haystack.length()){
            return -1;
        }
        List<Integer> firstCharMatch = new ArrayList<>();
        int firstIndex = 0;
        while (firstIndex <= haystack.length()-needle.length()){
            if (haystack.charAt(firstIndex) == needle.charAt(0)){
                int secondIndex = firstIndex;
                for (int i = 0; i < needle.length(); i++){
                    if (secondIndex >= haystack.length() || haystack.charAt(secondIndex) != needle.charAt(i)){
                        break;
                    }
                    if (haystack.charAt(secondIndex) == needle.charAt(0) && i != 0){
                        firstCharMatch.add(secondIndex);
                    }
                    if (i == needle.length()-1){
                        return firstIndex;
                    }
                    secondIndex ++;
                }

                if (firstCharMatch.size() != 0) {
                    firstIndex = firstCharMatch.get(0);
                    firstCharMatch.remove(0);
                }else{
                    firstIndex = secondIndex;
                }
            }else if (firstCharMatch.size() != 0){
                firstIndex = firstCharMatch.get(0);
                firstCharMatch.remove(0);
            } else {
                firstIndex ++;
            }
        }
        return -1;
    }

    //Actually time complexity is same as above. The difference is very minimal. As without the list, at most we just need to iterate extra needle.length()
    public int strStrMoreElegant(String haystack, String needle) {
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i + j)) break;
            }
        }
    }
}
