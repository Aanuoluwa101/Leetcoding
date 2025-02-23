"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

from linked_list import LinkedList, Node


def merge_two_lists(list1, list2):
    head = Node(None)
    tail = head 

    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1 
            list1 = list1.next 
        else:
            tail.next = list2 
            list2 = list2.next 
        tail = tail.next 
    
    if list1:
        tail.next = list1 
    elif list2:
        tail.next = list2 
    return head.next 
        

def print_list(head):
    temp_node = head
    values = [] 
    while temp_node:
        values.append(temp_node.value)
        temp_node = temp_node.next
        
    print(values)

if __name__ == "__main__":
    ll = LinkedList() 
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(4)

    ll2 = LinkedList() 
    ll2.insert_at_end(1)
    ll2.insert_at_end(3)
    ll2.insert_at_end(4)

    ll.print_list()
    ll2.print_list()

    merged = merge_two_lists(ll.head, ll2.head)
    print_list(merged)
    