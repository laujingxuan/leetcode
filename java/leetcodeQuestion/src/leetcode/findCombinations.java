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

        for (int i=addedLargest+1; i<=n; i++){
            List<Integer> newList = new ArrayList<>(current);
            newList.add(i);
            findCombination(found, newList, i, n, k-1);
        }
    }
}