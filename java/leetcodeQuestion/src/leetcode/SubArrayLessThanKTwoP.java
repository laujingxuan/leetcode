package leetcode;

import java.util.ArrayList;
import java.util.List;

public class SubArrayLessThanKTwoP {
    public static void main(String[] args) {
        System.out.println(numSubarrayProductLessThanK(new int[] { 10, 5, 2, 6 }, 100));
    }

//    The idea is always keep an max-product-window less than K;
//    Every time shift window by adding a new number on the right(j), if the product is greater than k, then try to reduce numbers on the left(i), until the subarray product fit less than k again, (subarray could be empty);
//    Each step introduces x new subarrays, where x is the size of the current window (j + 1 - i);
//    example: for window (5, 2), when 6 is introduced, it add 3 new subarray: (5, (2, (6)))
    public static int numSubarrayProductLessThanKEfficient(int[] nums, int k) {
        if (k == 0) return 0;
        int cnt = 0;
        int pro = 1;
        for (int i = 0, j = 0; j < nums.length; j++) {
            pro *= nums[j];
            while (i <= j && pro >= k) {
                pro /= nums[i++];
            }
            cnt += j - i + 1;
        }
        return cnt;
    }


    //time complexity of N^2. Not efficient
    public static int numSubarrayProductLessThanK(int[] nums, int k) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            System.out.println("Num: " + nums[i]);
            if (nums[i] < k) {
                int secondIndex = i + 1;
                int product = nums[i];
                count++;
                while (secondIndex < nums.length) {
                    System.out.print(product + ";");
                    product *= nums[secondIndex];
                    if (product >= k) {
                        break;
                    }
                    count++;
                    secondIndex++;
                }
            }
            System.out.println();
        }
        return count;
    }
}
