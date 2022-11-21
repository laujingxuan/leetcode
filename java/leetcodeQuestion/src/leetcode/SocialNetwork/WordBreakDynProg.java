package leetcode.SocialNetwork;

import java.util.*;

public class WordBreakDynProg {

    public static void main(String[] args) {
        System.out.println(wordBreak("catscatdog", new ArrayList<>(Arrays.asList("cat","cats","dog"))));
    }

    public static boolean wordBreak(String s, List<String> wordDict) {
        Map<Character, List<String>> dict = new HashMap<>();
        for (String string:wordDict){
            List<String> foundList = dict.get(string.charAt(0));
            if (foundList == null){
                foundList = new ArrayList<>();
            }
            foundList.add(string);
            dict.put(string.charAt(0), foundList);
        }

        HashSet<String> memo = new HashSet<>();

        return checkDictionary(s, dict, memo);
    }

    //sample solution. Cleaner way of implementation and smaller space complexity
    public boolean wordBreakAlternate(String s, List<String> wordDict) {
        // put all words into a hashset
        Set<String> set = new HashSet<>(wordDict);
        return wb(s, set);
    }

    private boolean wb(String s, Set<String> set) {
        int len = s.length();
        if (len == 0) {
            return true;
        }
        for (int i = 1; i <= len; ++i) {
            if (set.contains(s.substring(0, i)) && wb(s.substring(i), set)) {
                return true;
            }
        }
        return false;
    }

    public static boolean checkDictionary(String s, Map<Character, List<String>> dict, HashSet<String> memo){
        if (s == ""){
            return true;
        }
        List<String> matchingWords = dict.get(s.charAt(0));
        if (memo.contains(s) || matchingWords == null){
            return false;
        }
        boolean found = false;
        for (String word: matchingWords){
            int lengthOfWords = word.length();
            if (s.length() >= word.length()){
                String sub = s.substring(0,lengthOfWords);
                if (sub.equals(word)){
                    found = checkDictionary(s.substring(lengthOfWords, s.length()), dict, memo);
                }
                if (found){
                    break;
                }
            }
        }
        memo.add(s);
        return found;
    }
}
