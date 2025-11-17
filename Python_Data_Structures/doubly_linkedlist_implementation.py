# Implement Following functions for a doubly Linked List:
# 1. insert_at_Beginning
# 2. insert_at_end
# 3. insert_at
# 4. insert_values
# 5. insert_after_value
# 6. remove_at
# 7. remove_by_value
# 8. remove_head
# 9. remove_tail
# 10. print_forward
# 11. print_backward
# 12. get_length
# 13. search (T/F, return idx)



class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class Doubly_linkedList:
    def __init__(self, head = None):
        self.head = head
        
    def print_forward(self):
        itr = self.head
        while itr:
            print(itr.data, end = "->")
            itr = itr.next
        print(None)
    
    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data, end = "<-")
            itr = itr.prev
        print("head")
        
        
    def insert_at_beginning(self, data):
        new_node = Node(data, next = self.head, prev = None)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        
    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, prev = itr)
        

if __name__ == "__main__":
    my_doubly_list = Doubly_linkedList()
    my_doubly_list.insert_at_beginning(1)
    my_doubly_list.insert_at_end(4)
    my_doubly_list.print_forward()
    my_doubly_list.print_backward()
    