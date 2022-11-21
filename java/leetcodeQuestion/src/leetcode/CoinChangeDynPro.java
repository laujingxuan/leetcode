package leetcode;

import java.util.HashSet;
import java.util.Set;

import javax.print.attribute.HashAttributeSet;

public class CoinChangeDynPro {
    public static void main(String[] args) {
        int[] coins = new int[] { 1, 2, 5 };
        System.out.println(coinChange(coins, 11));
    }

    // You are given an integer array coins representing coins of different
    // denominations and an integer amount representing a total amount of money.
    // Return the fewest number of coins that you need to make up that amount. If
    // that amount of money cannot be made up by any combination of the coins,
    // return -1.
    // You may assume that you have an infinite number of each kind of coin.
    public static int coinChange(int[] coins, int amount) {
        Set<Integer> checkSet = new HashSet<>();
        int maximumValue = 0;
        for (int i = 0; i < coins.length; i++) {
            checkSet.add(coins[i]);
            maximumValue = Math.max(maximumValue, coins[i]);
        }
        return helperCoin(checkSet, amount, maximumValue);
    }

    public static int helperCoin(Set<Integer> coins, int amount, int maximumCoin) {
        if (amount <= 0) {
            return 0;
        }
        if (amount <= maximumCoin) {
            if (coins.contains(amount)) {
                return 1;
            } else {
                return -1;
            }
        }

        int fewestCoin = Integer.MAX_VALUE;
        for (int coin : coins) {
            int foundCoins = helperCoin(coins, amount - coin, maximumCoin);
            if (foundCoins > 0) {
                fewestCoin = Math.min(fewestCoin, helperCoin(coins, amount - coin, maximumCoin));
            }
        }
        if (fewestCoin == Integer.MAX_VALUE) {
            return -1;
        }
        return fewestCoin + 1;
    }
}
