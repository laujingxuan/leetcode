package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class MinimumSumTriangleDynPro {
    public static void main(String[] args) {
        List<List<Integer>> triangle = new ArrayList<>();
        triangle.add(new ArrayList<Integer>(Arrays.asList(2)));
        triangle.add(new ArrayList<Integer>(Arrays.asList(3,4)));
        triangle.add(new ArrayList<Integer>(Arrays.asList(6,5,7)));
        triangle.add(new ArrayList<Integer>(Arrays.asList(4,1,8,3)));
        System.out.println(minimumTotalBottomUp(triangle));
        System.out.println(minimumTotalTopDown(triangle));
    }

    public static int minimumTotalBottomUp(List<List<Integer>> triangle) {
        int m = triangle.size();
        int minTrackArray [] = new int [m];
        //copy all the values in the last row of triangle into the minTrackArray
        for (int i = 0; i < triangle.size(); i ++) {
            minTrackArray[i] = triangle.get(m-1).get(i);
        }

        //start from second last row
        for (int layer = m-2; layer>=0; layer --){
            //loop through each of the element and update the min path for that element accordingly
            for (int j=0; j<=layer; j++){
                minTrackArray[j] = Math.min(minTrackArray[j], minTrackArray[j+1]) + triangle.get(layer).get(j);
            }
        }
        return minTrackArray[0];
    }

    public static int minimumTotalTopDown(List<List<Integer>> triangle) {
        int m = triangle.size();
        if (m==0){
            return 0;
        } else if (m==1){
            return triangle.get(0).get(0);
        }
        int[] minTrackArray = new int [m];
        minTrackArray[0] = triangle.get(0).get(0);
        int min = Integer.MAX_VALUE;
        for (int layer = 1; layer < m; layer ++){
            //Need to calculate from behind since you will need to use the j-1 value of previous layer in the calculation
            for (int j = layer; j >=0; j --){
                if (j == 0){
                    minTrackArray[j] =minTrackArray[j] + triangle.get(layer).get(j);
                } else if (j == layer) {
                    minTrackArray[j] = minTrackArray[j-1] + triangle.get(layer).get(j);
                } else {
                    minTrackArray[j] = Math.min(minTrackArray[j-1], minTrackArray[j]) + triangle.get(layer).get(j);
                }

                if (layer == m-1){
                    min = Math.min(min, minTrackArray[j]);
                }
            }
        }

        return min;
    }
}
