class ListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next

def has_cycle(head: ListNode):
    seen = set()  # O(1) average access time
    temp = head 
    while temp:
        if temp in seen:
            return True 
        seen.append(temp)
        temp = temp.next
    return False