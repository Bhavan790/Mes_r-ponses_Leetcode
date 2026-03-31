class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null || left == right) return head;

        // Use a dummy node to simplify cases where left = 1
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode temp = dummy;
        ListNode prev = null, l = null, r = null;
        int s = 0; // Starting at 0 because of dummy

        // 1. Find the key nodes
        while(temp != null){
            if(s == left - 1) prev = temp;
            if(s == left) l = temp;
            if(s == right) r = temp;
            temp = temp.next;
            s++;
        }

        // Guard against out-of-bounds left/right
        if(l == null || r == null) return head;

        // 2. Reverse sublist
        ListNode curr = l;
        ListNode ans = r.next; // The tail connection
        ListNode stopNode = r.next; 

        while(curr != stopNode){
            ListNode nextnode = curr.next;
            curr.next = ans ;
            ans = curr;
            curr = nextnode;
        }

        // 3. Reconnect to the main list
        prev.next = r;

        return dummy.next;
    }
}