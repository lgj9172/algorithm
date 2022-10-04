class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        next_node = head.next
        total = 0
        while True:
            if next_node == None:
                break
            if next_node.val > 0 :
                total += next_node.val
            elif next_node.val == 0:
                curr_node = curr_node.next
                curr_node.val = total
                total = 0
            next_node = next_node.next
        curr_node.next = None
        return head.next