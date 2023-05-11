package leetcode;
// You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

// We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

// nums1[i] == nums2[j], and
// the line we draw does not intersect any other connecting (non-horizontal) line.
// Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

// Return the maximum number of connecting lines we can draw in this way.
class Solution {

    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int[][] memo = new int[nums1.length + 1][nums2.length + 1];
        for (int i = 1; i <= nums1.length; i++) {
            for (int j = 1; j <= nums2.length; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    memo[i][j] = memo[i - 1][j - 1] + 1;
                } else {
                    memo[i][j] = Math.max(memo[i - 1][j], memo[i][j - 1]);
                }
            }
        }
        return memo[nums1.length][nums2.length];
    }

    // Non ideal as exceed the time limit
    public int maxUncrossedLinesNonIdeal(int[] nums1, int[] nums2) {
        return dfsCheck(nums1, nums2, 0, nums1.length - 1, 0, nums2.length - 1);
    }

    public int dfsCheck(int[] nums1, int[] nums2, int start1, int end1, int start2, int end2) {
        int maxCount = 0;
        for (int i = start1; i >= 0 && i <= end1; i++) {
            for (int j = start2; j >= 0 && j <= end2; j++) {
                if (nums1[i] == nums2[j]) {
                    maxCount = Math.max(maxCount, 1 + dfsCheck(nums1, nums2, start1, i - 1, start2, j - 1)
                            + dfsCheck(nums1, nums2, i + 1, end1, j + 1, end2));
                }
            }
        }
        return maxCount;
    }
}