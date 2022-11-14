package leetcode;

public class MagicIndexRecursion {
    public static void main(String[] args) {
        System.out.println(magicIndexDistinctNumber(new int[]{-4,-2,0,2,4,6,8,9,10,55}));
        System.out.println(magicIndexNonDistNum(new int[]{-2,-1,0,4,5,5,9}));
    }

    //the input is sorted
    public static int magicIndexDistinctNumber(int[] input){
        return magicIndexDistNumHelper(input, 0, input.length-1);
    }

    public static int magicIndexDistNumHelper(int[] input, int start, int end){
        if (end < start){
            return -1;
        }
        int midIndex = (end + start)/2;
        int midValue = input[midIndex];
        if (midValue == midIndex){
            return midIndex;
        }
        if (midValue > midIndex){
            return magicIndexDistNumHelper(input, start, midIndex-1);
        } else {
            return magicIndexDistNumHelper(input, midIndex+1, end);
        }
    }

    //the input is sorted
    public static int magicIndexNonDistNum(int[] input){
        return magicIndexNonDistNumHelper(input, 0, input.length-1);
    }

    public static int magicIndexNonDistNumHelper(int[] input, int start, int end){
        if (end < start){
            return -1;
        }
        int midIndex = (end + start)/2;
        int midValue = input[midIndex];
        if (midValue == midIndex){
            return midIndex;
        }
        int rightCheck = magicIndexNonDistNumHelper(input, Math.max(midIndex+1, midValue), end);
        if (rightCheck >0){
            return rightCheck;
        }
        int leftCheck = magicIndexNonDistNumHelper(input, start, Math.min(midIndex-1, midValue));
        return leftCheck;
    }

}
