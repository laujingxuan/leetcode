package leetcode;

public class MaximumSubArray {
    public static void main(String[] args) {
        // System.out.println(maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
        System.out.println(maxSubArray(new int[] { 5, 4, -1, 7, 8 }));
    }

    public static int maxSubArray(int[] nums) {
        int largestNegativeNum = Integer.MIN_VALUE;
        int secondPointer = 0;
        int negativeSum = 0;
        int positiveSum = 0;
        int maxSum = 0;
        boolean isAllNegative = true;
        while (secondPointer < nums.length) {
            System.out.println("positiveSum:" + positiveSum);
            System.out.println("negativeSum:" + negativeSum);
            System.out.println("maxSum:" + maxSum);
            if (nums[secondPointer] >= 0) {
                isAllNegative = false;
                positiveSum += nums[secondPointer];
                if (positiveSum + negativeSum > maxSum) {
                    maxSum = positiveSum + negativeSum;
                }
            } else {
                if (nums[secondPointer] > largestNegativeNum) {
                    largestNegativeNum = nums[secondPointer];
                }
                negativeSum += nums[secondPointer];
                if (positiveSum + negativeSum < 0) {
                    negativeSum = 0;
                    positiveSum = 0;
                }
            }
            secondPointer++;
        }
        if (isAllNegative) {
            return largestNegativeNum;
        }
        return maxSum;
    }
}
