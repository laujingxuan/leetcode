package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class FindAnagramsSlidWind {
    public static void main(String[] args) {
        System.out.println(findAnagramsSlidWindow("cbaebabacd", "abc"));
    }

    // Given two strings s and p, return an array of all the start indices of p's
    // anagrams in s. You may return the answer in any order.

    // An Anagram is a word or phrase formed by rearranging the letters of a
    // different word or phrase, typically using all the original letters exactly
    // once.
    public static List<Integer> findAnagrams(String s, String p) {
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

    public static List<Integer> findAnagramsSlidWindow(String s, String p) {
        if (p.length() > s.length()) {
            return new ArrayList<Integer>();
        }
        HashMap<Character, Integer> pRecord = new HashMap<>();
        for (int i = 0; i < p.length(); i++) {
            if (pRecord.containsKey(p.charAt(i))) {
                int newCount = pRecord.get(p.charAt(i)) + 1;
                if (newCount == 0) {
                    pRecord.remove(p.charAt(i));
                } else {
                    pRecord.put(p.charAt(i), newCount);
                }
            } else {
                pRecord.put(p.charAt(i), 1);
            }
            if (pRecord.containsKey(s.charAt(i))) {
                int newCount = pRecord.get(s.charAt(i)) - 1;
                if (newCount == 0) {
                    pRecord.remove(s.charAt(i));
                } else {
                    pRecord.put(s.charAt(i), newCount);
                }
            } else {
                pRecord.put(s.charAt(i), -1);
            }
        }
        List<Integer> indexes = new ArrayList<>();
        if (pRecord.size() == 0) {
            indexes.add(0);
        }
        for (int i = 1; i < s.length() - p.length() + 1; i++) {
            char removeChar = s.charAt(i - 1);
            if (pRecord.get(removeChar) != null) {
                int newCount = pRecord.get(removeChar) + 1;
                if (newCount == 0) {
                    pRecord.remove(removeChar);
                } else {
                    pRecord.put(removeChar, newCount);
                }
            }else{
                pRecord.put(removeChar, 1);
            }
            char addChar = s.charAt(i + p.length() - 1);
            if (pRecord.get(addChar) != null) {
                int newCount = pRecord.get(addChar) - 1;
                if (newCount == 0){
                    pRecord.remove(addChar);
                }else{
                    pRecord.put(addChar, newCount);
                }
            }else{
                pRecord.put(addChar, -1);
            }
            if (pRecord.size() == 0){
                indexes.add(i);
            }
        }
        return indexes;
    }

    public List<Integer> findAnagramsTidierArrayMethod(String s, String p) {
        List<Integer> list = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;

        int[] hash = new int[256]; //character hash

        //record each character in p to hash
        for (char c : p.toCharArray()) {
            hash[c]++;
        }
        //two points, initialize count to p's length
        int left = 0, right = 0, count = p.length();

        while (right < s.length()) {
            //move right everytime, if the character exists in p's hash, decrease the count
            //current hash value >= 1 means the character is existing in p
            if (hash[s.charAt(right)] >= 1) {
                count--;
            }
            hash[s.charAt(right)]--;
            right++;

            //when the count is down to 0, means we found the right anagram
            //then add window's left to result list
            if (count == 0) {
                list.add(left);
            }
            //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
            //++ to reset the hash because we kicked out the left
            //only increase the count if the character is in p
            //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
            if (right - left == p.length() ) {

                if (hash[s.charAt(left)] >= 0) {
                    count++;
                }
                hash[s.charAt(left)]++;
                left++;
            }
        }
        return list;
    }
}
