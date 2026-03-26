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
    public ListNode middleNode(ListNode head) {
        /*/ ListNode temp=head;
        int count=0;
        while(temp!=null){
            count+=1;
            temp=temp.next;
        }
        int s=0;
        if(count%2==0)
            s=2;
        else
            s=1;
        ListNode ans=head;
        while(s!=count){
            ans=ans.next;
            count--;
            s++;
        }
        return ans; /*/
        int count = 0;
        ListNode temp = head;
        while(temp != null){
            count++;
            temp = temp.next;
        }

        // Step 2: Walk to middle
        int steps = count / 2;  // integer division
        ListNode ans = head;
        for(int i = 0; i < steps; i++){
            ans = ans.next;
        }

        return ans;

    }
}