package leetcode;

import java.util.Arrays;

public class SurroundedRegionsDFS {
    public static void main(String[] args) {
        char[][] input = new char[][] { { 'X', 'X', 'X', 'X' }, { 'X', 'O', 'O', 'X'
        }, { 'X', 'X', 'O', 'X' },
                { 'X', 'O', 'X', 'X' } };
        solve(input);
        System.out.println(Arrays.deepToString(input));
    }

    public static void solve(char[][] board) {
        int rowLength = board.length;
        int columnLength = board[0].length;
        for (int j = 0; j < columnLength; j++) {
            if (board[0][j] == 'O') {
                isFlipHelper(board, 0, j);
            }
            if (board[rowLength - 1][j] == 'O') {
                isFlipHelper(board, rowLength - 1, j);
            }
        }
        for (int i = 0; i < rowLength; i++) {
            if (board[i][0] == 'O') {
                isFlipHelper(board, i, 0);
            }
            if (board[i][columnLength - 1] == 'O') {
                isFlipHelper(board, i, columnLength - 1);
            }
        }
        for (int i = 0; i < rowLength; i++) {
            for (int j = 0; j < columnLength; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == '*') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    static int[][] checkArray = new int[][] { { 0, 1 }, { 1, 0 }, { -1, 0 }, { 0, -1 } };

    public static void isFlipHelper(char[][] board, int row, int column) {
        if (row < 0 || column < 0 || row >= board.length || column >= board[0].length || board[row][column] == 'X'
                || board[row][column] == '*') {
            return;
        }
        board[row][column] = '*';
        for (int i = 0; i < checkArray.length; i++) {
            int[] combi = checkArray[i];
            isFlipHelper(board, row + combi[0], column + combi[1]);
        }
    }
}
