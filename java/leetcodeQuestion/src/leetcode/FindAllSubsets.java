package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class FindAllSubsets {

    public static void main(String[] args) {
        int[] input = new int[] { 1, 2, 3 };
        System.out.println(Arrays.deepToString(subsets(input).toArray()));
    }

    // BETTER!!
    public static List<List<Integer>> backtrackSubsets(int[] nums) {
        List<List<Integer>> foundSubset = new ArrayList<>();
        backtrackSubsetsHelper(foundSubset, new ArrayList<>(), nums, 0);
        return foundSubset;
    }

    public static void backtrackSubsetsHelper(List<List<Integer>> foundSubset, List<Integer> currentCombi, int[] nums,
            int startIndex) {
        foundSubset.add(new ArrayList<>(currentCombi));
        if (startIndex >= nums.length) {
            return;
        }
        for (int i = startIndex; i < nums.length; i++) {
            currentCombi.add(nums[i]);
            backtrackSubsetsHelper(foundSubset, currentCombi, nums, i + 1);
            currentCombi.remove(currentCombi.size() - 1);
        }
    }

    // NOT EFFICIENT WAY
    public static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> foundSubset = new ArrayList<>();
        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }
        subsetsHelper(foundSubset, numList, new ArrayList<>());
        foundSubset.add(new ArrayList<>());
        return foundSubset;
    }

    public static void subsetsHelper(List<List<Integer>> foundSubset, List<Integer> nums, List<Integer> currentCombi) {
        if (nums.size() == 0) {
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            List<Integer> copy = new ArrayList<>(currentCombi);
            copy.add(nums.get(i));
            foundSubset.add(copy);
            List<Integer> copyOfNums = new ArrayList<>();
            for (int j = i + 1; j < nums.size(); j++) {
                copyOfNums.add(nums.get(j));
            }
            System.out.println(Arrays.deepToString(copyOfNums.toArray()));
            subsetsHelper(foundSubset, copyOfNums, copy);
        }
    }

}
