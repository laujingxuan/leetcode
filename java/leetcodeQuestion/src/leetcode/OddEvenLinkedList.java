package leetcode;

public class OddEvenLinkedList {
    public static void main(String[] args) {
        ListNode fifthNode = new ListNode(5);
        ListNode forthNode = new ListNode(4, fifthNode);
        ListNode thirdNode = new ListNode(3, forthNode);
        ListNode secondNode = new ListNode(2, thirdNode);
        ListNode firstNode = new ListNode(1, secondNode);
        printAllListNode(oddEvenList(firstNode));
    }

    public static void printAllListNode(ListNode input) {
        while (input != null) {
            System.out.println(input.val);
            input = input.next;
        }
    }

    public static ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode oddCurrent = head;
        ListNode evenHead = head.next;
        ListNode evenCurrent = head.next;
        ListNode current = evenHead.next;
        int index = 3;
        while (current != null) {
            if (index % 2 == 1) {
                oddCurrent.next = current;
                oddCurrent = current;
            } else {
                evenCurrent.next = current;
                evenCurrent = current;
            }
            index++;
            current = current.next;
        }
        oddCurrent.next = evenHead;
        evenCurrent.next = null;
        return head;
    }
}
