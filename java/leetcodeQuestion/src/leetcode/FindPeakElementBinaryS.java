package leetcode;

public class FindPeakElementBinaryS {
    public static void main(String[] args) {
        System.out.println(findPeakElement(new int[] { 1 }));
    }

    public static int findPeakElement(int[] nums) {
        int firstIndex = 0;
        int lastIndex = nums.length - 1;
        while (lastIndex > firstIndex) {
            int midIndex = (firstIndex + lastIndex) / 2;
            int midValue = nums[midIndex];
            boolean isLargerThanNext = true;
            boolean isLargerThanPrevious = true;
            if ((midIndex + 1 < nums.length) && midValue < nums[midIndex + 1]) {
                isLargerThanNext = false;
            }
            if ((midIndex - 1 >= 0) && midValue < nums[midIndex - 1]) {
                isLargerThanPrevious = false;
            }
            if (isLargerThanNext && isLargerThanPrevious) {
                return midIndex;
            }
            if (isLargerThanNext) {
                lastIndex = midIndex - 1;
            } else {
                firstIndex = midIndex + 1;
            }
        }
        return firstIndex;
    }
}
