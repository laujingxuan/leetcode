package leetcode;

import java.util.Arrays;

public class climbStairsDynPro {
    public static void main(String[] args) {
        System.out.println(climbStairs(20));
        System.out.println(climbStairsWithoutRecur(20));
    }

    public static int climbStairs(int n){
        int[] memo = new int[n+1];
        return climbStairsHelper(n, memo);
    }

    //for case of n=0 will return 0
    public static int climbStairsHelper(int n, int[]memo){
        if (n==0 || n==1 || n==2){
            return n;
        }else if (n==3){
            return 4;
        }
        if (memo[n] == 0){
            memo[n] = climbStairsHelper(n-1, memo) + climbStairsHelper(n-2, memo) + climbStairsHelper(n-3, memo);
        }
        return memo[n];
    }

    //for case of n=0 will return 1
    public static int climbStairsHelperAlt(int n, int[]memo){
        if (n<0){
            return 0;
        }else if (n==0){
            return 1;
        }
        if (memo[n] == 0){
            memo[n] = climbStairsHelper(n-1, memo) + climbStairsHelper(n-2, memo) + climbStairsHelper(n-3, memo);
        }
        return memo[n];
    }

    public static int climbStairsWithoutRecur(int n){
        if (n==0 || n==1 || n==2){
            return n;
        }else if (n==3){
            return 4;
        }
        int oneStepBefore = 4;
        int twoStepBefore = 2;
        int threeStepBefore = 1;
        int totalWays = 0;
        for (int i = 3; i < n; i++){
            totalWays = oneStepBefore + twoStepBefore + threeStepBefore;
            threeStepBefore = twoStepBefore;
            twoStepBefore = oneStepBefore;
            oneStepBefore = totalWays;
        }
        return totalWays;
    }
}
