package leetcode;

import java.util.HashMap;

public class IsomorphicString {
    public static void main(String[] args) {

    }

    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        if (s.length() == 1) {
            return true;
        }
        HashMap<Character, Character> checkMapForS = new HashMap<>();
        HashMap<Character, Character> checkMapForT = new HashMap<>();
        for (int i = 0; i < s.length(); i ++){
            if (checkMapForS.get(s.charAt(i)) == null && checkMapForT.get(t.charAt(i)) == null) {
                checkMapForS.put(s.charAt(i), t.charAt(i));
                checkMapForT.put(t.charAt(i), s.charAt(i));
            } else if (checkMapForS.get(s.charAt(i)) == null || checkMapForT.get(t.charAt(i)) == null){
                return false;
            } else if (checkMapForS.get(s.charAt(i)) != t.charAt(i) || checkMapForT.get(t.charAt(i)) != s.charAt(i)){
                return false;
            }
        }

        return true;
    }

    //without using Map
    public boolean isIsomorphicWithoutMap(String s, String t) {
        int m1[] = new int[256];
        int m2[] = new int[256];
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (m1[s.charAt(i)] != m2[t.charAt(i)]) return false;
            m1[s.charAt(i)] = i + 1;
            m2[t.charAt(i)] = i + 1;
        }
        return true;
    }
}
