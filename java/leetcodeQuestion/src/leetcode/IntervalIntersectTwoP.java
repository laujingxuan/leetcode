package leetcode;

import java.util.ArrayList;
import java.util.List;

public class IntervalIntersectTwoP {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int firstIndex = 0;
        int secondIndex = 0;
        List<int[]> listOfArrays = new ArrayList<>();
        while ((firstIndex < firstList.length) && (secondIndex < secondList.length)){
            int[] firstArray = firstList[firstIndex];
            int[] secondArray = secondList[secondIndex];
            if (firstArray[0] >= secondArray[0] && firstArray[0] <= secondArray[1]){
                if (firstArray[1] <= secondArray[1]){
                    listOfArrays.add(firstArray);
                    firstIndex ++;
                    continue;
                }else{
                    listOfArrays.add(new int[]{firstArray[0], secondArray[1]});
                    secondIndex ++;
                    continue;
                }
            } else if (secondArray[0] >= firstArray[0] && secondArray[0] <= firstArray[1]){
                if (secondArray[1] <= firstArray[1]){
                    listOfArrays.add(secondArray);
                    secondIndex ++;
                    continue;
                } else {
                    listOfArrays.add(new int[]{secondArray[0], firstArray[1]});
                    firstIndex ++;
                    continue;
                }
            }
            if (firstArray[0] < secondArray[0]){
                firstIndex ++;
                continue;
            }
            secondIndex ++;
        }
        int[][] toReturn = new int[listOfArrays.size()][];
        listOfArrays.toArray(toReturn);
        return toReturn;
    }
}
