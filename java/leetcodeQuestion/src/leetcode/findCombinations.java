package leetcode;
import java.util.ArrayList;
import java.util.List;

class findCombinations {
    public static void main(String[] args) {
        
    }

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> answer = new ArrayList<>();
        findCombination(answer, new ArrayList<>(), 0, n, k);
        return answer;
    }

    public void findCombination(List<List<Integer>> found, List<Integer> current, int addedLargest, int n, int k) {
        if (k ==0){
            found.add(current);
            return;
        }

        if (k>n-addedLargest){
            return;
        }

        int copiedOptions = n;
        for (int i=0; i<n-addedLargest; i++){
            List<Integer> newList = new ArrayList<>(current);
            newList.add(copiedOptions);
            findCombination(found, newList, copiedOptions, n, k-1);
            copiedOptions--;
        }
    }
}