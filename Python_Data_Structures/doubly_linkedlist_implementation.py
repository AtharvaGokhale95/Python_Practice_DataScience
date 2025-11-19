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
            print(itr.data, end = " <-> ")
            itr = itr.next
        print(None)
    
    def print_backward(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data, end = " <-> ")
            itr = itr.prev
        print("None")
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        
        
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
        
    def insert_at(self, data, idx):
        if idx < 0 or idx >= self.get_length():
            print("Index is out of range")
        
        if idx == 0:
            self.insert_at_beginning(data)
            
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                new_node = Node(data, next = itr.next, prev = itr)
                if itr.next:
                    itr.next.prev = new_node
                itr.next = new_node
                return
            itr = itr.next
            count += 1
    
    def insert_values(self, list_values):
        for value in list_values:
            self.insert_at_end(value)
        
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert, next = itr.next, prev = itr)
                if itr.next:
                    itr.next.prev = new_node
                itr.next = new_node
            itr = itr.next
            
    
            

if __name__ == "__main__":
    my_doubly_list = Doubly_linkedList()
    my_doubly_list.insert_at_beginning(1)
    my_doubly_list.insert_at_end(9)
    my_doubly_list.insert_at(4, 1)
    my_doubly_list.insert_values([16, 36])
    my_doubly_list.insert_after_value(16, 25)
    my_doubly_list.print_forward()
    my_doubly_list.print_backward()
    print(my_doubly_list.get_length())
    