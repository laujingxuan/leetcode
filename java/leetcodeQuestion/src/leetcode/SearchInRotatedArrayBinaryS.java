package leetcode;

//You must write an algorithm with O(log n) runtime complexity.
public class SearchInRotatedArrayBinaryS {
    public static void main(String[] args) {
        // System.out.println(search(new int[] { 4, 5, 6, 7, 0, 1, 2 }, 0));
        // System.out.println(search(new int[] { 4, 5, 6, 7, 8, 1, 2, 3 }, 8));
        System.out.println(search(new int[] { 4, 5, 6, 7, 8, 1, 2, 3 }, 8));
    }

    public static int search(int[] nums, int target) {
        if (nums.length == 0) {
            return -1;
        }
        int minimumPointIndex = searchMinimumValue(nums);
        int firstIndex = minimumPointIndex;
        int lastIndex = nums.length - 1;
        if (target > nums[lastIndex]) {
            firstIndex = 0;
            lastIndex = minimumPointIndex - 1;
        }
        while (firstIndex <= lastIndex) {
            int midIndex = (firstIndex + lastIndex) / 2;
            int midValue = nums[midIndex];
            if (midValue == target) {
                return midIndex;
            }
            if (midValue < target) {
                firstIndex = midIndex + 1;
            } else {
                lastIndex = midIndex - 1;
            }
        }
        return -1;
    }

    // smallest value
    public static int searchMinimumValue(int[] nums) {
        if (nums.length == 0) {
            return -1;
        }
        int firstIndex = 0;
        int lastIndex = nums.length - 1;
        while (firstIndex < lastIndex) {
            int lastValue = nums[lastIndex];
            int midIndex = (firstIndex + lastIndex) / 2;
            int midValue = nums[midIndex];
            if (midValue > lastValue) {
                firstIndex = midIndex + 1;
            } else {
                lastIndex = midIndex;
            }
        }
        return lastIndex;
    }

    // Alternate better and cleaner solution
    public int searchOneBinarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0)
            return -1;
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            // target and mid are on the same side
            if ((nums[mid] - nums[nums.length - 1]) * (target - nums[nums.length - 1]) > 0) {
                if (nums[mid] < target)
                    lo = mid + 1;
                else
                    hi = mid;
            } else if (target > nums[nums.length - 1])
                hi = mid; // target on the left side
            else
                lo = mid + 1; // target on the right side
        }
        // now hi == lo
        return nums[lo] == target ? lo : -1;
    }
}
