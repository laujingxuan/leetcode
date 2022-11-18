package leetcode;

public class FindProvisionsDFS {

    // time complexity might be 2MN since i might need to loop through a particular
    // row twice
    public int findCircleNumNotEfficient(int[][] isConnected) {
        int count = 0;
        for (int row = 0; row < isConnected.length; row++) {
            count += floodWithZeroes(isConnected, row);
        }
        return count;
    }

    public int floodWithZeroes(int[][] isConnected, int row) {
        boolean hasCount = false;
        int count = 0;
        for (int column = 0; column < isConnected[row].length; column++) {
            if (isConnected[row][column] == 1) {
                isConnected[row][column] = 0;
                if (!hasCount) {
                    count = 1;
                }
                if (column != row) {
                    floodWithZeroes(isConnected, column);
                }
            }
        }
        return count;
    }

    // time complexity only MN at the worst case
    public int findCircleNum(int[][] isConnected) {
        int[] hasVisited = new int[isConnected.length];
        int count = 0;
        for (int row = 0; row < isConnected.length; row++) {
            if (hasVisited[row] == 0) {
                count++;
                dfs(isConnected, row, hasVisited);
            }
        }
        return count;
    }

    public void dfs(int[][] isConnected, int row, int[] hasVisited) {
        for (int column = 0; column < isConnected[row].length; column++) {
            if (isConnected[row][column] == 1 && hasVisited[column] == 0) {
                hasVisited[column] = 1;
                dfs(isConnected, column, hasVisited);
            }
        }
        return;
    }
}
