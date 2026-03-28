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
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        ArrayList <Integer> s = new ArrayList<>();
        for(int i=0;i<lists.length;i++){
            ListNode current = lists[i];
            while(current!=null){
                s.add(current.val);
                current=current.next;
            }
        }
        Collections.sort(s);
        ListNode ans = new ListNode(0);
        ListNode temp = ans;
        for(int i=0;i<s.size();i++){
            temp.next = new ListNode(s.get(i));
            temp = temp.next;
        }
        return ans.next ;
    }
}