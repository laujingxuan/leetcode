package leetcode;

import java.util.Arrays;

public class LongestRepeatCharSlidWin {
    public static void main(String[] args) {
        System.out.println(characterReplacement("ABAB", 2));
    }

    public static int characterReplacement(String s, int k) {
        // has 26 characters
        int[] checkList = new int[26];
        int maxLength = 0;
        int maxCurrent = 0;
        int startIndex = 0;
        int endIndex = 0;
        while (endIndex < s.length()) {
            int tempNewCount = checkList[s.charAt(endIndex) - 'A'] + 1;
            checkList[s.charAt(endIndex) - 'A'] = tempNewCount;
            maxCurrent = Math.max(maxCurrent, tempNewCount);
            if (endIndex - startIndex + 1 - maxCurrent > k) {
                checkList[s.charAt(startIndex) - 'A'] = checkList[s.charAt(startIndex) - 'A'] - 1;
                startIndex++;
            }
            maxLength = Math.max(maxLength, endIndex - startIndex + 1);
            endIndex++;
        }
        return maxLength;
    }
}
