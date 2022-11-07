package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// /105. Construct Binary Tree from Preorder and Inorder Traversal
public class BinaryTreeFromPreAndInTra {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }
        int rootVal = preorder[0];
        TreeNode root = new TreeNode(rootVal);
        List<Integer> leftSideValues = new ArrayList();
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == rootVal) {
                break;
            }
            leftSideValues.add(inorder[i]);
        }
        int numberOfLeft = leftSideValues.size();
        root.left = buildTree(Arrays.copyOfRange(preorder, 0, numberOfLeft),
                Arrays.copyOfRange(inorder, 1, 1 + numberOfLeft));
        root.right = buildTree(Arrays.copyOfRange(preorder, numberOfLeft + 1, preorder.length),
                Arrays.copyOfRange(inorder, 1 + numberOfLeft, inorder.length));
        return root;
    }

}
