package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

//Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
public class generateParentheses {
    public static void main(String[] args) {
        List<String> output = generateParenthesis(3);
        System.out.println(Arrays.toString(output.toArray()));
    }

    public static List<String> generateParenthesis(int n){
        List<String> output = new ArrayList<>();
        helperGenerate(output, 0, 0, n, "");
        return output;
    }

    public static void helperGenerate(List<String> store, int openCount, int closeCount, int maxPair, String combination){
        if (combination.length() == 2 * maxPair){
            store.add(combination);
            return;
        }

        if (openCount < maxPair){
            helperGenerate(store, openCount + 1, closeCount, maxPair, combination + "(");
        }
        if (closeCount < openCount){
            helperGenerate(store, openCount, closeCount + 1, maxPair, combination + ")");
        }
    }
}
