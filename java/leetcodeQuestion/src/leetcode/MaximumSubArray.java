package leetcode;

public class MaximumSubArray {
    public static void main(String[] args) {
        // System.out.println(maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
        System.out.println(maxSubArray(new int[] { 5, 4, -1, 7, 8 }));
    }

    public static int maxSubArray(int[] nums) {
        if (nums.length == 0){
            return -1;
        }
        int pointer = 0;
        int negativeSum = 0;
        int positiveSum = 0;
        int maxSum = nums[0];
        while (pointer < nums.length) {
            System.out.println("positiveSum:" + positiveSum);
            System.out.println("negativeSum:" + negativeSum);
            System.out.println("maxSum:" + maxSum);
            if (nums[pointer] >= 0) {
                positiveSum += nums[pointer];
            } else {
                negativeSum += nums[pointer];
            }
            maxSum = Math.max(positiveSum + negativeSum, maxSum);
            if (positiveSum + negativeSum < 0) {
                negativeSum = 0;
                positiveSum = 0;
            }
            pointer++;
        }
        return maxSum;
    }

    //Same idea but recursion way of doing
    public static int maxSubArrayRecursion(int[] nums) {
        if (nums.length == 0){
            return -1;
        }
        int[] tracking = new int[nums.length];
        tracking[0] = nums[0];
        int currentMax = nums[0];
        for (int i = 1; i < nums.length; i ++){
            tracking[i] = Math.max(tracking[i-1]+nums[i], nums[i]);
            currentMax = Math.max(currentMax, tracking[i]);
        }
        return currentMax;
    }
}
