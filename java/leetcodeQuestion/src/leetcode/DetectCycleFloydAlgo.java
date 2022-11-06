package leetcode;

public class DetectCycleFloydAlgo {

    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slower = head;
        ListNode faster = head;
        while (faster != null) {
            slower = slower.next;
            if (faster.next == null) {
                return null;
            }
            faster = faster.next.next;
            if (faster == slower) {
                break;
            }
        }

        if (faster == null) {
            return null;
        }
        while (head != faster) {
            head = head.next;
            faster = faster.next;
        }
        return head;
    }
}
