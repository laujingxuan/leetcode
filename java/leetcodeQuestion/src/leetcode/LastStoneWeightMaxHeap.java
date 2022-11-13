package leetcode;

import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class LastStoneWeightMaxHeap {
    public static void main(String[] args) {
        System.out.println(lastStoneWeight(new int[]{3,7,8}));
    }

    //time complexity: nlogn
    public static int lastStoneWeightMaxHeapBetterSol(int[] stones){
        PriorityQueue<Integer> pQueue = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < stones.length; i ++){
            pQueue.add(stones[i]);
        }
        while (pQueue.size() > 1){
            int maxVal = pQueue.poll();
            int secondMax = pQueue.poll();
            if (maxVal > secondMax){
                pQueue.add(maxVal - secondMax);
            }
        }
        if (pQueue.size() == 0){
            return 0;
        }
        return pQueue.poll();
    }

    public static int lastStoneWeight(int[] stones) {
        if (stones.length == 0){
            return 0;
        } else if (stones.length == 1){
            return stones[0];
        }

        int tempMax = stones[0];
        int maxIndex = 0;
        int secondMax = 0;
        int secIndex = 0;
        int returnIndex = 0;
        for (int i = stones.length-2; i >=0 ; i --){
            for (int j = 1; j < stones.length; j ++){
                if (stones[j] >= secondMax){
                    secondMax = stones[j];
                    secIndex = j;
                    if (stones[j] >= tempMax){
                        secondMax = tempMax;
                        secIndex = maxIndex;
                        tempMax = stones[j];
                        maxIndex = j;
                    }
                }
            }
            System.out.println(stones[maxIndex]);
            System.out.println(stones[secIndex]);
            stones[maxIndex] = Math.abs(stones[maxIndex] - stones[secIndex]);
            stones[secIndex] = 0;
            System.out.println(Arrays.toString(stones));
            returnIndex = maxIndex;
            tempMax = stones[0];
            maxIndex = 0;
            secondMax = 0;
            secIndex = 0;
        }

        return stones[returnIndex];
    }
}
