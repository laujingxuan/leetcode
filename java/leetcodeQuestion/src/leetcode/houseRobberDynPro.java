package leetcode;

import java.util.Arrays;

public class houseRobberDynPro {
    public static void main(String[] args) {
        int[] input = {1,2,3,1};
        int[] memo = new int[input.length];
        Arrays.fill(memo, -1);
        System.out.println(robRecursiveDP(input, memo, input.length-1));
    }

    public static int rob(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        if (nums.length == 1){
            return nums[0];
        }
        if (nums.length == 2){
            if (nums[0] > nums[1]) {
                return nums[0];
            }
            return nums[1];
        }

        int largestSumBeforeTwoValues =  nums[0];
        int largestSumBeforeOneValue = nums[0];
        if (nums[1] > nums[0]) {
            largestSumBeforeOneValue = nums[1];
        }
        for (int i = 2; i < nums.length; i ++){
            int temp = largestSumBeforeOneValue;
            if (largestSumBeforeTwoValues + nums[i] > largestSumBeforeOneValue) {
                largestSumBeforeOneValue = largestSumBeforeTwoValues + nums[i];
            }
            largestSumBeforeTwoValues = temp;
        }

        return largestSumBeforeOneValue;
    }

    public static int robRecursiveDP(int[] nums, int[]memo, int index) {
        if (index < 0){
            return 0;
        }
        if (memo[index] > -1){
            return memo[index];
        }
        memo[index] = Math.max(robRecursiveDP(nums, memo, index-1), robRecursiveDP(nums, memo, index-2) + nums[index]);
        return memo[index];
    }
}
