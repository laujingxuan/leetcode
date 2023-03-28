package leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class TestConcept {

    public static int[] findSum(int[] array, int target){
        int left = 0;
        int right = array.length - 1;

        while (right > left){
            if (array[left] + array[right] == target){
                break;
            } else if (array[left] + array[right] < target){
                left += 1;
            } else {
                right -= 1;
            }
        }

        while (right - 1 > left && array[right] == array[right - 1]){
            right -= 1;
        }
        return new int[]{left,right};
    }

    public static void main(String[] args) {
            int[] array = new int[]{0, 1,3,5,5,7,9};
            System.out.println(Arrays.toString(findSum(array, 6)));
//          PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>();
//          pQueue.add(10);
//          pQueue.add(8);
//          pQueue.add(9);
//          pQueue.add(7);
//          while(pQueue.size() != 0){
//              System.out.println(pQueue.poll());
//          }
    }
}
