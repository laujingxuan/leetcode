package leetcode;

public class fibonacci {
    public static void main(String[] args) {
        int n = 50;
//        System.out.println(fibonacci(n));
        int[] memo = new int[n + 1];
        System.out.println(fibonacciDynamicProgram(n, memo));
    }

    public static int fibonacci(int n) {
        if (n == 0 || n == 1) {
            return n;
        }

        return fibonacci(n-1) + fibonacci(n-2);
    }

    public static int fibonacciDynamicProgram(int n, int[] memo) {
        if (n == 0 || n == 1){
            memo[n] = n;
            return n;
        }

        if (memo[n] == 0){
            memo[n] = fibonacciDynamicProgram(n - 1, memo) + fibonacciDynamicProgram(n -2, memo);
        }
        return memo[n];
    }
}

