package leetcode;

import java.util.*;

public class FourSum {

    public static void main(String[] args) {
//        int[] input = {1,0,-1,0,-2,2};
//        List<List<Integer>> ans = fourSum(input, 0);
//        System.out.println(Arrays.deepToString(ans.toArray()));
//        int[] input1 = {-3,-2,-1,0,0,1,2,3};
//        List<List<Integer>> ans1 = fourSum(input1, 0);
//        System.out.println(Arrays.deepToString(ans1.toArray()));
        int[] input3 = {1000000000,1000000000,1000000000,1000000000};
//        List<List<Integer>> ans3 = fourSum(input3, -294967296);
//        System.out.println(Arrays.deepToString(ans3.toArray()));
        FourSum test = new FourSum();
        List<List<Integer>> ans4 = test.recursionFourSum(input3, 0);
        System.out.println(Arrays.deepToString(ans4.toArray()));
    }
    //Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that
    //0 <= a, b, c, d < n
    //a, b, c, and d are distinct.
    //nums[a] + nums[b] + nums[c] + nums[d] == target
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        Set<List<Integer>> foundSet = new HashSet<>();
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < nums.length-3; i++) {
            for (int j = i+1; j< nums.length-2; j++){
                int firstPointer = j + 1;
                int lastPointer = nums.length-1;
                while (lastPointer > firstPointer){
                    long check = (long)nums[i] + (long)nums[j] + (long)nums[firstPointer] + (long)nums[lastPointer];
                    if (check>Integer.MAX_VALUE){
                        lastPointer --;
                        continue;
                    } else if (check < Integer.MIN_VALUE){
                        firstPointer ++;
                        continue;
                    }
                    if (nums[i] + nums[j] + nums[firstPointer] + nums[lastPointer] == target){
                        List<Integer> temp = new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[firstPointer], nums[lastPointer]));
                        foundSet.add(temp);
                    }
                    if (nums[i] + nums[j] + nums[firstPointer] + nums[lastPointer] > target){
                        lastPointer --;
                        continue;
                    }
                    firstPointer ++;
                }
            }
        }
        for (List<Integer> t: foundSet){
            ans.add(t);
        }
        return ans;
    }

    int len = 0;
    public List<List<Integer>> recursionFourSum(int[] nums, int target) {
        len = nums.length;
        Arrays.sort(nums);
        return kSum(nums, target, 4, 0);
    }
    private ArrayList<List<Integer>> kSum(int[] nums, int target, int k, int index) {
        ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
        if(index >= len) {
            return res;
        }
        if(k == 2) {
            int i = index, j = len - 1;
            while(i < j) {
                //find a pair
                if(target - nums[i] == nums[j]) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(target-nums[i]);
                    res.add(temp);
                    //skip duplication
                    while(i<j && nums[i]==nums[i+1]) i++;
                    while(i<j && nums[j-1]==nums[j]) j--;
                    i++;
                    j--;
                    //move left bound
                } else if (target - nums[i] > nums[j]) {
                    i++;
                    //move right bound
                } else {
                    j--;
                }
            }
        } else{
            for (int i = index; i < len - k + 1; i++) {
                //use current number to reduce ksum into k-1sum
                ArrayList<List<Integer>> temp = kSum(nums, target - nums[i], k-1, i+1);
                if(temp != null){
                    //add previous results
                    for (List<Integer> t : temp) {
                        long total = 0;
                        for (int p: t){
                            total += (long)p;
                        }
                        if (total >= Integer.MIN_VALUE && total <= Integer.MAX_VALUE){
                            t.add(0, nums[i]);
                        }
                    }
                    res.addAll(temp);
                }
                while (i < len-1 && nums[i] == nums[i+1]) {
                    //skip duplicated numbers
                    i++;
                }
            }
        }
        return res;
    }
}
