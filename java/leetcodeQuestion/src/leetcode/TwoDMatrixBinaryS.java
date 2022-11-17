package leetcode;

public class TwoDMatrixBinaryS {

    // time complexity = matrix.length + log(matrix[0].length)
    public boolean searchMatrix(int[][] matrix, int target) {
        int targetRow = matrix.length - 1;
        for (int i = 0; i < matrix.length - 1; i++) {
            if (target >= matrix[i][0] && target < matrix[i + 1][0]) {
                targetRow = i;
                break;
            }
        }

        int firstIndex = 0;
        int lastIndex = matrix[targetRow].length - 1;
        while (lastIndex >= firstIndex) {
            int midIndex = (firstIndex + lastIndex) / 2;
            if (matrix[targetRow][midIndex] == target) {
                return true;
            }

            if (matrix[targetRow][midIndex] > target) {
                lastIndex = midIndex - 1;
            } else {
                firstIndex = midIndex + 1;
            }
        }
        return false;
    }

    public boolean searchMatrixBetterBinarySearch(int[][] matrix, int target) {
        int n = matrix.length;
        int m = matrix[0].length;
        int l = 0, r = m * n - 1;
        while (l != r) {
            int mid = (l + r - 1) >> 1;
            if (matrix[mid / m][mid % m] < target)
                l = mid + 1;
            else
                r = mid;
        }
        return matrix[r / m][r % m] == target;
    }
}
