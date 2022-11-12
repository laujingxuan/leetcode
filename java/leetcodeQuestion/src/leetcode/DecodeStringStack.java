package leetcode;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Stack;

public class DecodeStringStack {
    public static void main(String[] args) {
        System.out.println(decodeString("3[a]2[bc]"));
        System.out.println(decodeString("3[a2[c]]"));
        System.out.println(decodeString("2[abc]3[cd]ef"));
        System.out.println(decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"));
        System.out.println(decodeStringWithQueueRecursive("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"));
        System.out.println(decodeStringWithStack("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"));
    }

    public static String decodeString(String s) {
        StringBuilder overall = new StringBuilder();
        for (int i = 0; i < s.length(); i ++){
            if (Character.isDigit(s.charAt(i))){
                int count = 0;
                while (Character.isDigit(s.charAt(i))){
                    count = (count * 10) + Integer.valueOf(s.substring(i, i+1));
                    i++;
                }
                i = i+1;
                int startingIndex = i;
                int endingIndex = i+1;
                int countOfOpen = 1;
                while (countOfOpen != 0){
                    if (s.charAt(endingIndex)=='['){
                        countOfOpen++;
                    }
                    if (s.charAt(endingIndex) == ']'){
                        countOfOpen--;
                    }
                    endingIndex++;
                }
                endingIndex--;
                String fullSubString = decodeString(s.substring(startingIndex, endingIndex));
                for (int j = 0; j < count; j++){
                    overall.append(fullSubString);
                }
                i = endingIndex;
                continue;
            }
            if (Character.isLetter(s.charAt(i))){
                overall.append(s.charAt(i));
            }
        }
        return overall.toString();
    }

    //idea similar to my solution by cleaner implementation
    public static String decodeStringWithQueueRecursive(String s) {
        Deque<Character> queue = new LinkedList<>();
        for (char c : s.toCharArray()) queue.offer(c);
        return helper(queue);
    }

    public static String helper(Deque<Character> queue) {
        StringBuilder sb = new StringBuilder();
        int num = 0;
        while (!queue.isEmpty()) {
            char c= queue.poll();
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '[') {
                String sub = helper(queue);
                for (int i = 0; i < num; i++) sb.append(sub);
                num = 0;
            } else if (c == ']') {
                break;
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public static String decodeStringWithStack(String s) {
        String res = "";
        Stack<Integer> countStack = new Stack<>();
        Stack<String> resStack = new Stack<>();
        int index = 0;
        while (index < s.length()){
            if (Character.isDigit(s.charAt(index))){
                int count = 0;
                while (Character.isDigit(s.charAt(index))){
                    count = count * 10 + s.charAt(index) - '0';
                    index++;
                }
                countStack.push(count);
            } else if (s.charAt(index) == '['){
                resStack.push(res);
                res = "";
                index ++;
            } else if (s.charAt(index) == ']'){
                int count = countStack.pop();
                StringBuilder sb = new StringBuilder(resStack.pop());
                for (int i = 0; i < count; i++){
                    sb.append(res);
                }
                res = sb.toString();
                index ++;
            } else {
                res += s.charAt(index);
                index ++;
            }
        }
        return res;
    }

}
