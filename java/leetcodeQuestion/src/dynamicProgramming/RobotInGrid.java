package dynamicProgramming;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;

public class RobotInGrid {
    public static void main(String[] args) {
        boolean[][] data = new boolean[][]{
                {true, false, true, true},
                {true, false, true, true},
                {true, true, true, true},
                {true, true, true, true}
        };
        System.out.println(Arrays.toString(getPath(data).toArray()));
    }

    public static ArrayList<Point> getPath(boolean[][] maze){
        if (maze.length == 0 || maze[0].length == 0){
            return new ArrayList<Point>();
        }
        ArrayList<Point> foundPath = new ArrayList<>();
        int[][]memo = new int[maze.length][maze[0].length];
        if (getPathHelper(maze, maze.length-1, maze[0].length-1, foundPath, memo)){
            return foundPath;
        }
        return new ArrayList<Point>();
    }

    public static boolean getPathHelper(boolean[][] maze, int row, int column, ArrayList<Point> foundPath, int[][] memo){
        if (row < 0 || column < 0 || !maze[row][column]){
            return false;
        }
        if (memo[row][column] == 1){
            return true;
        }
        if (memo[row][column] == -1){
            return false;
        }
        System.out.println(row + ":" + column);
        if (isOrigin(row, column) || getPathHelper(maze, row - 1, column, foundPath, memo) || getPathHelper(maze, row, column - 1, foundPath, memo)){
            Point newPoint = new Point(row, column);
            foundPath.add(newPoint);
            memo[row][column] = 1;
            return true;
        }
        memo[row][column] = -1;
        return false;
    }

    public static boolean isOrigin(int row, int column){
        if (row == 0 && column == 0){
            return true;
        }
        return false;
    }
}
