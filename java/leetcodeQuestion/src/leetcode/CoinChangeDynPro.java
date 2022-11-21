package leetcode;

import java.util.HashSet;
import java.util.Set;

import javax.print.attribute.HashAttributeSet;

public class CoinChangeDynPro {
    public static void main(String[] args) {
        int[] coins = new int[] { 1,2,5 };
        System.out.println(coinChange(coins, 100));
    }

    // You are given an integer array coins representing coins of different
    // denominations and an integer amount representing a total amount of money.
    // Return the fewest number of coins that you need to make up that amount. If
    // that amount of money cannot be made up by any combination of the coins,
    // return -1.
    // You may assume that you have an infinite number of each kind of coin.
    public static int coinChange(int[] coins, int amount) {
        int[] memo = new int[amount + 1];
        return helperCoin(coins, amount, memo);
    }

    public static int helperCoin(int[] coins, int amount, int[] memo) {
        if (amount < 0) {
            return -1;
        }
        if (amount == 0){
            return 0;
        }
        if (memo[amount] != 0){
            return memo[amount];
        }

        int fewestCoin = Integer.MAX_VALUE;
        for (int coin : coins) {
            int foundCoins = helperCoin(coins, amount - coin, memo);
            if (foundCoins >= 0) {
                fewestCoin = Math.min(fewestCoin, foundCoins + 1);
            }
        }
        memo[amount] = fewestCoin;
        if (fewestCoin == Integer.MAX_VALUE) {
            memo[amount] = -1;
        }

        return memo[amount];
    }

    public static int coinChangeIterativeBottomUp(int[] coins, int amount) {
        int[] iterationCheck = new int[amount+1];
        int current = 1;
        while (current <= amount){
            int min = -1;
            for (int coin: coins){
                if (current >= coin && iterationCheck[current-coin] != -1){
                    int temp = iterationCheck[current-coin] + 1;
                    if (min == -1){
                        min = temp;
                    } else {
                        min = Math.min(temp, min);
                    }
                }
            }
            iterationCheck[current] = min;
            current++;
        }
        return iterationCheck[amount];
    }

    public static int helperCoinBottomUp(int[] coins, int amount) {
        int[] iterationCheck = new int[amount+1];
        int current = 0;
        while (current <= amount){
            int min = Integer.MAX_VALUE;
            for (int coin: coins){
                if (current >= coin && iterationCheck[amount-coin] != -1){
                    int temp = iterationCheck[amount-coin] + 1;
                    min = Math.min(temp, min);
                }
            }
            iterationCheck[current] = min;
            current++;
        }
        return iterationCheck[amount];
    }
}
