package leetcode;

// You are given the head of a linked list, and an integer k.
// Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
public class SwappingNodesInLinkedList {
    public ListNode swapNodes(ListNode head, int k) {
        if (head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode leftPrev = dummy;
        ListNode rightPrev = dummy;
        ListNode fast = head;
        int dupK = k;
        while (dupK > 0 && fast != null) {
            fast = fast.next;
            dupK -= 1;
        }

        while (fast != null) {
            k -= 1;
            if (k == 0) {
                leftPrev = rightPrev;
            }
            fast = fast.next;
            rightPrev = rightPrev.next;
        }

        if (k > 0) {
            k -= 1;
            leftPrev = rightPrev;
            while (k > 0) {
                leftPrev = leftPrev.next;
                k -= 1;
            }

        }

        // swap leftPrev.next and rightPrev.next
        ListNode leftNode = leftPrev.next;
        ListNode rightNode = rightPrev.next;

        // need to handle condition where leftPrev.next = rightPrev
        if (rightPrev == leftNode) {
            leftPrev.next = rightNode;
            leftNode.next = rightNode.next;
            rightNode.next = leftNode;
        } else {
            leftPrev.next = rightNode;
            rightPrev.next = leftNode;
            ListNode temp = rightNode.next;
            rightNode.next = leftNode.next;
            leftNode.next = temp;
        }

        return dummy.next;
    }

    public void printNodes(ListNode node) {
        while (node != null) {
            System.out.print(node.val + ",");
            node = node.next;
        }
        System.out.println();
    }
}
