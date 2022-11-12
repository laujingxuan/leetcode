package leetcode;

import java.util.Stack;

public class BackspaceCompareStack {
    public static void main(String[] args) {
//        System.out.println(backspaceCompare("abcd", "bbcd"));
        System.out.println(backspaceCompareBetterSolution("bxj##tw", "bxj###tw"));
    }

    //O(N) space and O(N) time
    public static boolean backspaceCompare(String s, String t) {
        Stack<Character> sStack = new Stack<>();
        for (int i = 0; i < s.length(); i ++){
            if (s.charAt(i) != '#'){
                sStack.push(s.charAt(i));
            }else if (sStack.size() != 0){
                sStack.pop();
            }
        }
        Stack<Character> tStack = new Stack<>();
        for (int i = 0; i < t.length(); i ++){
            if (t.charAt(i) != '#'){
                tStack.push(t.charAt(i));
            }else if (tStack.size() != 0){
                tStack.pop();
            }
        }
        if (sStack.size() != tStack.size()){
            return false;
        }
        System.out.println(sStack.size());
        while (!sStack.isEmpty()){
            Character temp1 = sStack.pop();
            Character temp2 = tStack.pop();
            System.out.println(temp1);
            System.out.println(temp2);
            if (temp1 != temp2){
                return false;
            }
        }
        return true;
    }

    //O(N) time and O(1) space by comparing backwards!
    public static boolean backspaceCompareBetterSolution(String s, String t) {
        int sIndex = s.length()-1;
        int tIndex = t.length()-1;
        while (true){
            int back = 0;
            while (sIndex >= 0 && (back > 0 || s.charAt(sIndex) == '#')){
                if (s.charAt(sIndex) == '#'){
                    back ++;
                } else {
                    back --;
                }
                sIndex --;
            }
            back = 0;
            while (tIndex >= 0 && (back > 0 || t.charAt(tIndex) == '#')){
                if (t.charAt(tIndex) == '#'){
                    back ++;
                }else {
                    back --;
                }
                tIndex --;
            }
            if ((tIndex < 0 || sIndex < 0) || s.charAt(sIndex) != t.charAt(tIndex)){
                break;
            }
            sIndex --;
            tIndex --;
        }
        if (tIndex>=0 || sIndex>=0){
            return false;
        }
        return true;
    }
}
