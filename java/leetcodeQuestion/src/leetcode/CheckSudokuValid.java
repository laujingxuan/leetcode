package leetcode;

import java.util.HashSet;
import java.util.Set;

public class CheckSudokuValid {
    public static boolean isValidSudoku(char[][] board) {
        Set<String> checkSet = new HashSet<>();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] != '.') {
                    int rowBlock = i / 3;
                    int columnBlock = j / 3;
                    if (!checkSet.add(i + "(" + board[i][j] + ")") || !checkSet.add("(" + board[i][j] + ")" + j)
                            || !checkSet.add(rowBlock + "(" + board[i][j] + ")" + columnBlock)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}
