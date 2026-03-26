/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }
        ListNode temp1=head;
        int count=1;
        while(temp1.next!=null){
            count++;
            temp1=temp1.next;
        }
        temp1.next=head;
        ListNode temp2=head;
        k=k%count;
        int steps=count-k-1;
        for(int i=0;i<steps;i++)
            temp2=temp2.next;
        ListNode newhead=temp2.next;
        temp2.next=null;
        return newhead;
    }
}