import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> temp = new ArrayList<>();
        List<List<Integer>> found = new ArrayList<>();
        backTrack(found, temp, nums);
        return found;
    }

    public void backTrack(List<List<Integer>> found, List<Integer> temp, int[] nums) {
        if (temp.size() == nums.length){
            found.add(new ArrayList<>(temp));
            return;
        }

        for (int i = 0; i < nums.length; i++){
            if (temp.contains(nums[i])){
                continue;
            }
            temp.add(nums[i]);
            backTrack(found, temp, nums);
            temp.remove(temp.size()-1);
        }
    }
}