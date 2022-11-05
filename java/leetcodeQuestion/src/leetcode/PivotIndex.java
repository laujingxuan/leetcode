package leetcode;

public class PivotIndex {
    public int pivotIndex(int[] nums) {
        int total = 0;
        int sum = 0;
        for (int i = 0; i < nums.length; i ++){
            total += nums[i];
        }

        for (int j = 0; j < nums.length; j++){
            if (sum*2 == total - nums[j]) {
                return j;
            }
            sum += nums[j];
        }
        return -1;
    }
}
