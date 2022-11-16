package leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> checkMap = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] charArray = new char[26];
            for (int j = 0; j < strs[i].length(); j++) {
                charArray[strs[i].charAt(j) - 'a']++;
            }
            String charString = new String(charArray);
            if (!checkMap.containsKey(charString)) {
                checkMap.put(charString, new ArrayList<>());
            }
            List<String> foundList = checkMap.get(charString);
            foundList.add(strs[i]);
        }
        return new ArrayList<>(checkMap.values());
    }
}
