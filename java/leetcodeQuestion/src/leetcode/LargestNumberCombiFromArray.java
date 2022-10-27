package leetcode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class LargestNumberCombiFromArray {
    public static void main(String[] args) {
        int[] nums = {3,30,34,5,9};
        System.out.println(largestNumber(nums));
    }

    public static String largestNumber(int[] nums) {
        if (IntStream.of(nums).sum() == 0){
            return "0";
        }

        String[] s_nums = new String[nums.length];

        for (int i = 0; i < nums.length; i ++){
            s_nums[i] = String.valueOf(nums[i]);
        }

        // Comparator to decide which string should come first in concatenation
        Comparator<String> comp = new Comparator<String>(){
            @Override
            public int compare(String str1, String str2){
                String s1 = str1 + str2;
                String s2 = str2 + str1;
                return s2.compareTo(s1); // reverse order here, so we can do append() later
            }
        };

        Arrays.sort(s_nums, comp);

        StringBuilder sb = new StringBuilder();
        for (String s: s_nums){
            sb.append(s);
        }
        return sb.toString();
    }
}
