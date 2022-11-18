package leetcode;

public class SubArrayLessThanTwoP {
    public static void main(String[] args) {
        System.out.println(numSubarrayProductLessThanK(new int[] { 10, 5, 2, 6 }, 100));
    }

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
