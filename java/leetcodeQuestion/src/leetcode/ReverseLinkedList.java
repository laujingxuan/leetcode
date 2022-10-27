package leetcode;

public class ReverseLinkedList {

    //Iterative solution
    public ListNode reverseList(ListNode head) {
        ListNode latestNode = null;
        ListNode current = head;
        while (current != null){
            ListNode temp = current.next;
            current.next = latestNode;
            latestNode = current;
            current = temp;
        }
        return latestNode;
    }

    //Recursive solution
    public ListNode reverseListRecursive(ListNode head) {
        /* recursive solution */
        return reverseListInt(head, null);
    }

    private ListNode reverseListInt(ListNode head, ListNode newHead) {
        if (head == null)
            return newHead;
        ListNode next = head.next;
        head.next = newHead;
        return reverseListInt(next, head);
    }

    public class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}
