package leetcode;

import java.util.Arrays;

public class mergeSort {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(sortArray(new int[] { 5, 3, 7, 8 })));
    }

    public static int[] sortArray(int[] nums) {
        return mergeSort(nums, 0, nums.length);
    }

    public static int[] mergeSort(int[] nums, int firstIndex, int lastIndex) {
        if (lastIndex - firstIndex <= 0) {
            return new int[0];
        }
        if (lastIndex - firstIndex == 1) {
            return new int[] { nums[firstIndex] };
        }
        int mid = (firstIndex + lastIndex) / 2;
        int[] leftSorted = mergeSort(nums, firstIndex, mid);
        int[] rightSorted = mergeSort(nums, mid, lastIndex);
        int[] finalSorted = new int[leftSorted.length + rightSorted.length];
        int a = 0;
        int b = 0;
        int c = 0;
        while (a < leftSorted.length && b < rightSorted.length) {
            if (leftSorted[a] > rightSorted[b]) {
                finalSorted[c] = rightSorted[b];
                b++;
            } else {
                finalSorted[c] = leftSorted[a];
                a++;
            }
            c++;
        }
        while (a < leftSorted.length) {
            finalSorted[c] = leftSorted[a];
            a++;
            c++;
        }
        while (b < rightSorted.length) {
            finalSorted[c] = rightSorted[b];
            b++;
            c++;
        }

        return finalSorted;
    }
}
