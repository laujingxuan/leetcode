package leetcode;

import java.util.Arrays;

public class removeArrayDuplicates {

    public static void main(String[] args) {
        int[] test = {1,1,2};
        System.out.println(removeArrayDuplicates(test));
        System.out.println(Arrays.toString(test));
    }

    public static int removeArrayDuplicates(int[] nums){
        int startingIndex = 0;
        int previousNum = Integer.MIN_VALUE;
        for (int i =0; i < nums.length; i ++){
            if (nums[i] != previousNum){
                nums[startingIndex] = nums[i];
                previousNum = nums[i];
                startingIndex ++;
            }
        }

        return startingIndex;
    }
}
