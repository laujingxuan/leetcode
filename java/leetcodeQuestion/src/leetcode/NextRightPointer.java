package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class NextRightPointer {
    public static void main(String[] args) {

    }

    public static Node connectDFS(Node root){
        if (root == null){
            return null;
        }
        if (root.left != null) {
            root.left.next = root.right;
            if (root.next != null){
                root.right.next = root.next.left;
            }
            connectDFS(root.left);
            connectDFS(root.right);
        }
        return root;
    }

    public static Node connectBFS(Node root){
        if (root == null){
            return null;
        }
        Queue<Node> queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()){
            for (int i = queue.size(); i >0; i --){
                Node retrieved = queue.poll();
                if (retrieved.left != null){
                    retrieved.left.next = retrieved.right;
                    if (retrieved.next != null){
                        retrieved.right.next = retrieved.next.left;
                    }
                    queue.add(retrieved.left);
                    queue.add(retrieved.right);
                }
            }
        }
        return root;
    }
}

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};