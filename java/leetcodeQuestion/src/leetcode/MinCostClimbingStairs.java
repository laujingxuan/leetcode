package leetcode;

import java.util.Arrays;

public class MinCostClimbingStairs {
    public static void main(String[] args) {
        int[] test = new int[] { 10, 15, 20 };
        System.out.println(minCostClimbingStairs(test));
    }

    public static int minCostClimbingStairs(int[] cost) {
        int[] minimumForAll = new int[cost.length + 1];
        Arrays.fill(minimumForAll, -1);
        minCostClimbingStairs(cost, minimumForAll, cost.length);
        return minimumForAll[cost.length];
    }

    public static int minCostClimbingStairs(int[] cost, int[] minimumForAll, int numberOfItem) {
        if (numberOfItem == 0 || numberOfItem == 1) {
            minimumForAll[numberOfItem] = 0;
            return minimumForAll[numberOfItem];
        }
        if (minimumForAll[numberOfItem] > -1) {
            return minimumForAll[numberOfItem];
        }
        minimumForAll[numberOfItem] = Math.min(
                cost[numberOfItem - 2] + minCostClimbingStairs(cost, minimumForAll, numberOfItem - 2),
                cost[numberOfItem - 1] + minCostClimbingStairs(cost, minimumForAll, numberOfItem - 1));

        return minimumForAll[numberOfItem];
    }

    // Bottom up computation - O(n) time, O(1) space
    public int minCostClimbingStairsIteration(int[] cost) {
        int n = cost.length;
        int first = cost[0];
        int second = cost[1];
        if (n <= 2)
            return Math.min(first, second);
        for (int i = 2; i < n; i++) {
            int curr = cost[i] + Math.min(first, second);
            first = second;
            second = curr;
        }
        return Math.min(first, second);
    }
}
