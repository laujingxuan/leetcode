package leetcode;

public class MinSubArrayLenSlidW {
    public static void main(String[] args) {
        System.out.println(minSubArrayLen(7, new int[] { 2, 3, 1, 2, 4, 3 }));
    }

    // Given an array of positive integers nums and a positive integer target,
    // return the minimal length of a subarray whose sum is greater than or equal to
    // target. If there is no such subarray, return 0 instead.
    public static int minSubArrayLen(int target, int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int firstIndex = 0;
        int secondIndex = 0;
        int tempSum = nums[0];
        int minimumLength = Integer.MAX_VALUE;
        while (true) {
            if (tempSum < target) {
                secondIndex++;
                if (secondIndex >= nums.length) {
                    break;
                }
                tempSum += nums[secondIndex];
                continue;
            }
            minimumLength = Math.min(minimumLength, secondIndex - firstIndex + 1);
            tempSum -= nums[firstIndex];
            firstIndex++;
        }
        if (minimumLength == Integer.MAX_VALUE) {
            return 0;
        }
        return minimumLength;
    }

    public static int minSubArrayLenAlternateCleanerCode(int target, int[] a) {
        if (a == null || a.length == 0)
            return 0;

        int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;

        while (j < a.length) {
            sum += a[j++];

            while (sum >= target) {
                min = Math.min(min, j - i);
                sum -= a[i++];
            }
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
