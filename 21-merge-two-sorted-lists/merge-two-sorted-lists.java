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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;
        ListNode temp=list1;
        while(temp.next!=null){
            temp=temp.next;
        }
        ListNode temp1=list1;
        ListNode temp2=null;
        temp.next=list2;
        for(;temp1!=null;temp1=temp1.next){
            for(temp2=temp1;temp2!=null;temp2=temp2.next){
                if(temp1.val>temp2.val){
                    int c=temp2.val;
                    temp2.val=temp1.val;
                    temp1.val=c;
                }
            }
        }
        return list1;
    }
}
// ok but o(n^2) need to solve in constant or atleast o(n)