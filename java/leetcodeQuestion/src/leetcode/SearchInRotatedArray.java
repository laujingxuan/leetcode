package leetcode;

public class SearchInRotatedArray {
    public static void main(String[] args) {
        // System.out.println(search(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 0));
        System.out.println(search(new int[] { 4, 5, 6, 7, 8, 1, 2, 3 }, 8));
    }

    public static int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        if (nums.length == 1) {
            if (nums[0] == target) {
                return 0;
            }
            return -1;
        }
        int firstIndex = 0;
        int lastIndex = nums.length - 1;
        while (firstIndex <= lastIndex) {
            int firstValue = nums[firstIndex];
            int lastValue = nums[lastIndex];
            int midIndex = (firstIndex + lastIndex) / 2;
            int midValue = nums[midIndex];
            System.out.println("firstValue: " + firstValue);
            System.out.println("lastValue: " + lastValue);
            // System.out.println("midIndex: " + midIndex);
            System.out.println("midValue: " + midValue);
            if (midValue == target) {
                return midIndex;
            } else {
                if (midValue < target && lastValue < target || midValue > target && target >= firstValue) {
                    lastIndex = midIndex - 1;
                } else {
                    firstIndex = midIndex + 1;
                }
            }
        }
        return -1;
    }
}
