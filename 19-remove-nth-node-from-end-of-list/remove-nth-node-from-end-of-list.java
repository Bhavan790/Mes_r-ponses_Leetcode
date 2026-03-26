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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null || (head.next == null && n == 1)) return null;
        int count=0;
        ListNode temp=head;
        while(temp!=null){
            count++;
            temp=temp.next;
        }
        int s=count-n;
        if (s == 0) return head.next;
        ListNode ans=head;
        ListNode pre=null;
        for(int i=0;i<s;i++){
            pre=ans;
            ans=ans.next;
        }
        pre.next=ans.next;
        return head;
    }
}