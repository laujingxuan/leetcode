package leetcode;

public class DeleteDuplicateLinkedListTwoP {

    public static void main(String[] args) {
        ListNode sevenNode = new ListNode(5);
        ListNode sixthNode = new ListNode(4, sevenNode);
        ListNode fifthNode = new ListNode(4, sixthNode);
        ListNode forthNode = new ListNode(3, fifthNode);
        ListNode thirdNode = new ListNode(3, forthNode);
        ListNode secondNode = new ListNode(2, thirdNode);
        ListNode firstNode = new ListNode(1, secondNode);
        // ListNode thirdNode = new ListNode(2);
        // ListNode secondNode = new ListNode(2, thirdNode);
        // ListNode firstNode = new ListNode(1, secondNode);
        printAllListNode(deleteDuplicatesBetter(firstNode));
    }

    public static void printAllListNode(ListNode input) {
        while (input != null) {
            System.out.print(input.val + " :");
            input = input.next;
        }
        System.out.println();
    }

    public static ListNode deleteDuplicatesBetter(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode slow = dummy;
        ListNode fast = head;
        while (fast != null) {
            while (fast.next != null && fast.next.val == fast.val) {
                fast = fast.next;
            }

            if (slow.next == fast) {
                slow = slow.next;
            } else {
                slow.next = fast.next;
            }
            fast = fast.next;
        }

        return dummy.next;
    }

    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode previousNode = null;
        ListNode currentNode = head;
        ListNode firstNode = null;
        if (currentNode.next.val != currentNode.val) {
            firstNode = currentNode;
            previousNode = currentNode;
        }
        while (currentNode.next != null && currentNode.next.next != null) {
            if (currentNode.val != currentNode.next.val && currentNode.next.val != currentNode.next.next.val) {
                System.out.println("currentNode.next.val: " + currentNode.next.val);
                if (firstNode != null) {
                    previousNode.next = currentNode.next;
                } else {
                    firstNode = currentNode.next;
                }
                previousNode = currentNode.next;
            }
            currentNode = currentNode.next;
        }

        if (currentNode.val != currentNode.next.val) {
            if (previousNode != null) {
                previousNode.next = currentNode.next;
            } else {
                firstNode = currentNode.next;
            }
        } else if (previousNode != null) {
            previousNode.next = null;
        }

        return firstNode;
    }
}
