# Implement Following functions for a Linked List:
# 1. insert_at_Beginning
# 2. insert_at_end
# 3. insert_at
# 4. insert_values
# 5. insert_after_value
# 6. remove_at
# 7. remove_by_value
# 8. remove_head
# 9. remove_tail
# 10. print
# 11. get_length
# 12. search (T/F, return idx)
# 13. reverse_inplace
# 14. is_palindrome


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def print(self):
        if self.head is None:
            print("The Linked List is empty")
            return
        
        itr = self.head
        # result = ""
        while itr:
            # result = result + str(itr.data) +  "->"
            print(itr.data, end = "->")
            itr = itr.next
        print(None)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
            
        
    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        
    def insert_at_end(self, data):
        itr = self.head
        while itr.next:
            itr = itr.next
        new_node = Node(data, None)
        itr.next = new_node
        
    def insert_at(self, data, idx):
        if idx < 0 or idx >= self.get_length():
            print("Out of range index")
            return
        
        if idx == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                new_node = Node(data, itr.next)
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
                new_node = Node(data_to_insert, itr.next)
                itr.next = new_node
                return
            itr = itr.next
            
    def remove_at(self, idx):
        if idx < 0 or idx >= self.get_length():
            print("Invalid Index")
        if idx == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1
            
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
            
    def remove_head(self):
        self.head = self.head.next
        
    def remove_tail(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None
        
    def search(self, data):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count += 1
                

if __name__ == '__main__':
    my_list = LinkedList()
    my_list.insert_at_beginning(1)
    my_list.insert_at_end(4)
    my_list.insert_at_end(16)
    my_list.insert_at(9, 2)
    my_list.insert_values([25, 49])
    my_list.insert_after_value(25, 36)
    # my_list.remove_at(2)
    # my_list.remove_by_value(49)
    # my_list.remove_head()
    # my_list.remove_tail()
    print("Index:", my_list.search(36))
    my_list.print()
    print(my_list.get_length())
    

# Notes:

# Way to use prev: 
# def insert_at_end(self, data):
#     itr = self.head
#     while itr:
#         prev = itr
#         itr = itr.next
#     prev.next = Node(data) 