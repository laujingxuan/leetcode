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

    public static boolean isValidSudokuAlternate(char [][] board){
        if (board.length == 0){
            return false;
        }
        for (int i = 0; i < board.length; i ++){
            Set<Character> rowSet = new HashSet<>();
            Set<Character> columnSet = new HashSet<>();
            Set<Character> blockSet = new HashSet<>();

            for (int j = 0; j < board[0].length; j++){
                if (board[j][i]!='.' && !rowSet.add(board[j][i])){
                    return false;
                }
                if(board[i][j] != '.' && !columnSet.add(board[i][j])){
                    return false;
                }
                //for i is 0 to 2, 3 blocks at the first row will be checked (0,0;0,1;0,2)
                //for i is 3 to 5, 3 blocks at the second row will be checked (1,0;1,1;1,2)
                //for i is 6 to 8, 3 blocks at the third row will be checked (2,0;2,1;2,2)
                int rowIndex = 3*(i/3);
                int columnIndex = 3*(i%3);
                if (board[rowIndex+j/3][columnIndex+j%3]!='.' && !blockSet.add(board[rowIndex+j/3][columnIndex+j%3])){
                    return false;
                }
            }
        }
        return true;
    }
}
