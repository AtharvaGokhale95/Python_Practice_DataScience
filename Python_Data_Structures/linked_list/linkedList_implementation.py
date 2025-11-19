# Properties/Parameters: data, next - These properties are passed as parameters to init function as the value is not fixed, and user decides the value while creating the obj of this class

# Methods: __init__()
class Node:
    # self is a reference/ pointer to the current object of the class (stores the memory address of the the current object created)
    def __init__(self, data = None, next = None):               # declared the properties with default values as None
        self.data = data    # When I refer data as self.data it helps create a attribute "data" for a any "Node" object - Parameter is used to initialize the attribute
        self.next = next

    # Property/ parameter: head - The value is not passed as parameters to the init function as the value is fixed, and the user does not decide the initial value 
    # If I would have passed head as a parameter, when a instance of class LinkedList is created, we need to pass the value for head 

# Methods: __init__, insert_at_beginning, insert_at_end
class LinkedList:   # A LL only have 1 property/ attribute: head
    
    def __init__(self, head = None):
        self.head = head        # We don't always use a parameter to initialize the attribute
    
    # We need a parameter for this function 
    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        # Creating a object of class Node - passed the value for both the properties of class Node
        # data: value passed to insert_at_beginning function
        # next: 
        #   1. We are now inserting a "new_node" at the beginning of a empty LL. There doesn't exit a next node and thus next = None. Currently head = None so next automatically becomes None
        #   2. We are now inserting a "new_node" at the beginning of a non-empty LL.
        #       data = data
        #       next = self.head (existing head of the non-empty LL, so that the new node is linked to th existing LL)
        #       head = new_node (so the new_node is now the first node of the LL)
        
        
        
        # head was initialized to None as the LL was empty. Now, as we have created a new node, we point the head to this node. 
        # So we are updating the value of the parameter of class Node
        self.head = new_node 
        
        
    def insert_at_end(self, data):
        # If the LL is empty -> Even this method will partly act as it is inserting the node at the beginning and thus self.head = new_node
        # However, as we want this node to be the last one, next = None 
        if self.head is None:
            self.head = Node(data, None)    # This can also be done as: new_node = Node(data, None) -> self.head = new_node
            return
        
        # If the LL is not empty -> We have iterate over the entire LL and reach at the current last node
        itr = self.head         # So now itr is a Node obj pointing to the head of the LL
        while itr.next:         # Until itr.next != None
            itr = itr.next      # Until itr.next have some value we will be iterating as we want to reach to the current last node in the LL
            # Once the itr.next = None, we will exist the while loop
        # Now we are the current last node, thus we want to point this current last node to the new_node we want to insert at the end
        itr.next = Node(data, None)
        
    def insert_at (self, idx, data):
        if idx < 0:
            print("Invalid Index")
        
        if idx == 0:
            self.insert_at_beginning(data)
        
        # As we inserting the node in between the LL: head is not required to be updated -> We only need to insert it at the right location and update the "next" attribute
        count = 0       # Track the current node idx while traversing the list
        itr = self.head
        while itr:      # Until itr != None 
            if count == idx - 1:
                # At this location: itr is pointing to the node after which we want to insert the new_node
                # itr.next -> The node which will be the node after the new_node. Thus, Node(data, itr.next)
                # Insert the new node here:
                new_node = Node(data, itr.next)
                itr.next = new_node         # itr is currently pointing at the earlier node. Thus, itr.next = new_node links the earlier node to the new_node
            itr = itr.next
            count += 1
        print("The index is greater than the size of the LL")       # If the provided idx is bigger than the size of LL, then we print this
                
            
        
    # Using this function, we will create a entire new LL using the list of values in data_list
    def insert_values(self, data_list):
        self.head = None        # Initialized it as a empty LL
        for value in data_list:
            self.insert_at_end(value)       # We use insert_at_end method to insert each value after the other
            
    
    def remove_at(self, idx):
        # If the index is out of range of the Linked List
        if idx < 0 or idx >= self.get_length():     # Eg: length = 6: if idx >= 6 then raise exception, if idx = 5 then it is a valid idx
            print("Invalid index")
        
        # If we want to remove the first node in the linked list
        if idx == 0:
            self.head = self.head.next          # Here the self.head is a obj of class Node: self.head = new_node (logic while inserting a new node)
            return 
        
        # If we want to remove the node at a particular idx
        count = 0
        itr = self.head
        while itr:
            if count == idx - 1:
                # We are at the node prior to the node which we want to remove
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
            
    def print(self):
        # If the LL is empty
        if self.head is None:
            print("The LL is empty")
            return
        
        # If the LL is not empty, self.head is pointing to a "Node" object (first node in LL). 
        # Thus, self.head is the "Node" object itself and any Node obj have data and next attributes
        # When we do: itr = self.head: This statement copies the same reference to itr (Now is also a Node obj) and also have data and next attributes
        itr = self.head 
        while itr:          # Iterating until itr != None
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

            
        
# Create a LL:
my_list = LinkedList()
new_list = LinkedList()

# Add new nodes at the beginning
my_list.insert_at_beginning(2)
my_list.insert_at_end(4)
my_list.insert_at_end(16)
my_list.insert_at(2, 9)
new_list.insert_values([1,2,4,9,16,25])


# Print the list
my_list.print()
new_list.print()

# Print the length of LL:
print(new_list.get_length())

# Remove a node at a index:
my_list.print()
my_list.remove_at(2)
my_list.print()

