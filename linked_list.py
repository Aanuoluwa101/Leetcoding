
class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value 
            self.next = None 
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, value):
        new_node = self.Node(value) 
        new_node.next = self.head 
        self.head = new_node 

    def insert_at_end(self, value):
        new_node = self.Node(value)
        # if not self.head:
        #     new_node.next = self.head 
        #     self.head = new_node
        #     return
            
        # temp_node = self.head 
        # while temp_node.next:
        #     temp_node = temp_node.next 
        
        # new_node = self.Node(value)
        # new_node.next = temp_node.next
        # temp_node.next = new_node 

        if not self.head: # list is empty 
            self.head = new_node
            return
        tail = self.head 
        while tail.next:
            tail = tail.next 
        tail.next = new_node

    def insert_at_index(self, index, value):
        temp_node = self.head
        prev_node = None 
        for _ in range(index):
            if temp_node.next:
                prev_node = temp_node 
                temp_node = temp_node.next
        new_node = self.Node(value)
        new_node.next = temp_node
        prev_node.next = new_node
        
        
        

    def print_list(self):
        temp_node = self.head
        values = [] 
        while temp_node:
            values.append(temp_node.value)
            temp_node = temp_node.next
        
        print(values)
        # print(self.head.value)

    def delete_at_begining(self):
        pass 

    def delete_at_end(self):
        pass 

    def delete_at_index(self):
        pass


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


if __name__ == "__main__":
    ll = LinkedList() 
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    ll.insert_at_end(3)
    ll.insert_at_beginning(0)
    ll.print_list()
