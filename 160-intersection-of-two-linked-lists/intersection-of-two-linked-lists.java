class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int count1 = 0;
        int count2 = 0;
        ListNode temp1 = headA;
        ListNode temp2 = headB;
        while(temp1 != null){
            count1++;
            temp1 = temp1.next;
        }
        while(temp2 != null){
            count2++;
            temp2 = temp2.next;
        }
        while(count1 > count2){
            count1--;
            headA = headA.next;
        }
        while(count2 > count1){
            count2--;
            headB = headB.next;
        }
        
        while(headA != headB){
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
}