package leetcode;

import java.util.*;

public class ShortestPathTwoDMatrixBFS {

    public static void main(String[] args) {
        System.out.println(shortestPathBinaryMatrix(new int[][]{{0,0,0}, {1,1,0}, {1,1,0}}));
//        Set<List<Integer>> hasVisited = new HashSet<>();
//        hasVisited.add(new ArrayList<>(Arrays.asList(0, 1)));
//        hasVisited.add(new ArrayList<>(Arrays.asList(1, 0)));
//        hasVisited.add(new ArrayList<>(Arrays.asList(1, 0)));
//        System.out.println(hasVisited.size());
    }

    public static int shortestPathBinaryMatrix(int[][] grid) {
        if (grid.length == 0){
            return 0;
        }
        Queue<int[]> checkQueue = new LinkedList<>();
        checkQueue.add(new int[]{0,0});
        Set<List<Integer>> hasVisited = new HashSet<>();
        int[][] checkList = new int[][]{{1, 0}, {0, 1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}, {-1, 0}, {0 , -1}};
        int shortestPath = 0;
        while (checkQueue.size() > 0){
            shortestPath ++;
            for (int j = checkQueue.size() ; j > 0 ; j --){
                int[] coordi = checkQueue.poll();
                int row = coordi[0];
                int column = coordi[1];
                if (grid[row][column] == 0){
                    if (row == grid.length- 1 && column == grid.length -1){
                        return shortestPath;
                    }
                    for (int i = 0; i < checkList.length; i ++){
                        int newRow = row + checkList[i][0];
                        int newColumn = column + checkList[i][1];
                        if (newColumn < grid.length && newRow < grid.length && newColumn >=0 && newRow >=0 && !hasVisited.contains(new ArrayList<>(Arrays.asList(newRow, newColumn)))){
                            hasVisited.add(new ArrayList<>(Arrays.asList(newRow, newColumn)));
                            checkQueue.add(new int[]{newRow, newColumn});
                        }
                    }
                }
            }
        }
        return -1;
    }
}
