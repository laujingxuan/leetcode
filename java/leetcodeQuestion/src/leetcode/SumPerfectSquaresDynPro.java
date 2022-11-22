package leetcode;

public class SumPerfectSquaresDynPro {

    public static void main(String[] args) {
        System.out.println(numSquares(12));
    }

    public static int numSquares(int n) {
        int[] memo = new int[n + 1];
        return numSquaresHelper(n, memo);
    }

    public static int numSquaresHelper(int n, int[] memo) {
        if (n < 0) {
            return -1;
        } else if (n == 0) {
            return 0;
        }
        if (memo[n] != 0) {
            return memo[n];
        }
        int maxPossibleSqrNum = (int) Math.sqrt((double) n);
        int leastNumberNeeded = Integer.MAX_VALUE;
        for (int i = 1; i <= maxPossibleSqrNum; i++) {
            int newN = n - (int) Math.pow(i, 2);
            int temp = numSquaresHelper(newN, memo);
            if (temp != -1) {
                leastNumberNeeded = Math.min(leastNumberNeeded, temp + 1);
            }
        }
        memo[n] = leastNumberNeeded;
        if (leastNumberNeeded == Integer.MAX_VALUE) {
            memo[n] = -1;
        }
        return memo[n];
    }
}
