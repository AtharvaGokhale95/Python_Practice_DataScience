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
        if self.head is None:
            print("Linked List is empty")
            return
        
        result = ""
        itr = self.head
        while itr:
            result = result + str(itr.data) + " <-> "
            itr = itr.next
        result += "None"
        return result
        
    def get_last_node(self):
        itr = self.head
        while itr.next:                 # This returns the actual last Node
            itr = itr.next
        return itr
    
    def print_backward(self):
        if self.head is None:
            print("Linked List if empty")
            return 
        
        result = ""
        itr = self.get_last_node()
        while itr:
            result += str(itr.data) + " <-> "
            itr = itr.prev
        result += "None"
        return result
        
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
        if self.head is None:
            self.insert_at_beginning()
            return 
        
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
            
    def remove_at(self, idx):
        if idx < 0 or idx >= self.get_length():
            print("Invalid Index")
            return
        
        if idx == 0:
            self.head = self.head.next
            self.head.prev = None
            return 
        
        # Consider the scenario of removing the last node
        count = 0
        itr = self.head
        while itr:
            if count == idx:
                itr.prev.next = itr.next        # Forward link
                if itr.next:
                    itr.next.prev = itr.prev    # Backward Link
                return
            itr = itr.next
            count += 1
            
    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return  # LL is empty
        
        if self.head.data == data_to_remove:    # Remove the first node
            if self.head.next:                  # If there are more than 1 node
                self.head = self.head.next
                self.head.prev = None
            else:                               # Only 1 node in the LL
                self.head = None                # Now the LL becomes empty
        
        # Remove the node somewhere in between the LL or the last node
        itr = self.head
        while itr:
            if itr.data == data_to_remove:
                itr.prev.next = itr.next        # This statement is valid even if itr.next is None - Forward Link
                # For the backward link: itr.next.prev - We need to check if itr.next exists (not None)
                if itr.next:
                    itr.next.prev = itr.prev    # Backward Link
                return 
            itr = itr.next
            
            
    def remove_head(self):                      # Remove the first element
        # If it is a empty LL
        if self.head is None:
            return
        
        # If there is only 1 node in the LL
        if self.head.next is None:
            self.head = None                    # Make it a empty LL after removing the only node
            
        # If there are more than 1 nodes     
        self.head = self.head.next              # Forward Link
        self.head.prev = None
        
    def remove_tail(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
        
        last_node = self.get_last_node()        
        itr = last_node                         # itr is at the last node
        itr.prev.next = None                    # Forward link: itr.prev -> None
        
    def search(self, data_to_search):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_to_search:
                return count
            itr = itr.next
            count += 1
        return -1           # If the value is not found

if __name__ == "__main__":
    my_doubly_list = Doubly_linkedList()
    my_doubly_list.insert_at_beginning(1)
    my_doubly_list.insert_at_end(9)
    my_doubly_list.insert_at(4, 1)
    my_doubly_list.insert_values([16, 36])
    my_doubly_list.insert_after_value(16, 25)
    print("Original LL:", my_doubly_list.print_forward())
    
    print(f"The index of the value 36 is:", my_doubly_list.search(36))
    
    my_doubly_list.remove_at(0)
    print("After removing the first element (Print Forward):", my_doubly_list.print_forward())
    print("After removing the first element (Print Backward):", my_doubly_list.print_backward())
    print("Length of LL:", my_doubly_list.get_length())
    
    my_doubly_list.remove_by_value(36)
    print("After removing the node with value 36 (Print Forward):",my_doubly_list.print_forward())
    print("After removing the node with value 36(Print Backward):",my_doubly_list.print_backward())
    print("Length of LL:",my_doubly_list.get_length())
    
    my_doubly_list.remove_head()
    print("After removing the head (Print Forward):",my_doubly_list.print_forward())
    print("After removing the head (Print Backward):",my_doubly_list.print_backward())
    print("Length of LL:",my_doubly_list.get_length())
    
    my_doubly_list.remove_tail()
    print("After removing the tail (Print Forward):",my_doubly_list.print_forward())
    print("After removing the tail (Print Backward):",my_doubly_list.print_backward())
    print("Length of LL:",my_doubly_list.get_length())
    
    