package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class FindAnagramsSlidWind {
    public static void main(String[] args) {

    }

    // Given two strings s and p, return an array of all the start indices of p's
    // anagrams in s. You may return the answer in any order.

    // An Anagram is a word or phrase formed by rearranging the letters of a
    // different word or phrase, typically using all the original letters exactly
    // once.
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> pRecord = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            if (pRecord.containsKey(p.charAt(i))) {
                pRecord.put(p.charAt(i), (pRecord.get(p.charAt(i)) + 1));
                continue;
            }
            pRecord.put(p.charAt(i), 1);
        }
        List<Integer> indexes = new ArrayList<>();
        for (int i = 0; i < s.length() - p.length() + 1; i++) {
            char current = s.charAt(i);
            if (pRecord.containsKey(current)) {
                HashMap tempMap = new HashMap<Character, Integer>(pRecord);
                boolean isFound = true;
                for (int j = i; j < p.length() + i; j++) {
                    if (!tempMap.containsKey(s.charAt(j))) {
                        isFound = false;
                        break;
                    }
                    int newCount = (Integer) tempMap.get(s.charAt(j)) - 1;
                    if (newCount == 0) {
                        tempMap.remove(s.charAt(j));
                    } else {
                        tempMap.put(s.charAt(j), newCount);
                    }
                }
                if (isFound) {
                    indexes.add(i);
                }
            }
        }
        return indexes;
    }
}
