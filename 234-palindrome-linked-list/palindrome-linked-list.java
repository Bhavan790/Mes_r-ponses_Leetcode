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
    public boolean isPalindrome(ListNode head) {
        int a=0;
        ListNode temp1 = head ;
        while(temp1!=null){
            a+=1;
            temp1=temp1.next;
        }
        int[] res = new int[a];
        int p=0;
        ListNode temp2 = head ;
        while(temp2!=null){
            res[p++]=temp2.val;
            temp2=temp2.next;
        }
        int l=0;
        int r=res.length-1;
        while(l<r){
            if(res[l]==res[r]){
                l++;
                r--;
            }
            else
                return false;
        }
        return true;
    } 
}