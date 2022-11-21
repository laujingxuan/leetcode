package leetcode;

import java.util.LinkedList;
import java.util.Queue;

public class NextRightPointer {
    public static void main(String[] args) {
        Node first = new Node(1);
        Node second = new Node(2);
        Node third = new Node(3);
        Node forth = new Node(4);
        Node fifth = new Node(5);
        Node sixth = new Node(6);
        Node seventh = new Node(7);
        first.left = second;
        first.right = third;
        second.left = forth;
        second.right = fifth;
        third.right = seventh;
        Node returnFrom = connect(first);
        printAllNodes(returnFrom);
    }

    public static void printAllNodes(Node root){
        Queue printQueue = new LinkedList<Node>();
        printQueue.add(root);
        while (printQueue.size() != 0){
            Node toPrint = (Node) printQueue.poll();
            System.out.print(toPrint.val + " : ");
            if (toPrint.left != null){
                printQueue.add(toPrint.left);
            }
            if (toPrint.right != null){
                printQueue.add(toPrint.right);
            }
        }
        System.out.println();
    }

    //Solution for non-complete binary tree
    public static Node connect(Node root) {
        Node dummyHead = new Node(0);
        Node pre = dummyHead;
        Node current = root;
        while (current != null){
            if (current.left != null){
                if (pre != null){
                    pre.next = current.left;
                }
                pre = current.left;
            }
            if (current.right != null){
                if (pre != null){
                    pre.next = current.right;
                }
                pre = current.right;
            }

            current = current.next;
            if (current == null) {
                current = dummyHead.next;
                pre = dummyHead;
                dummyHead.next = null;
            }
        }
        return root;
    }

    //Solution for complete binary tree only
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

    //Solution for complete binary tree only
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