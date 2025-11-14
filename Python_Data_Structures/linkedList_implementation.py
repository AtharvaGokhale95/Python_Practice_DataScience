

# Properties/ Parameters: data, next - These properties are passed as parameters to the __init__ function as the value is not fixed, 
# and you want the user of the class to decide the initial value

# Methods: __init__()
class Node:
    # self is a reference/ pointer to the current object of the class (stores the memory address of the the current object created)
    def __init__(self, data = None, next = None):               # declared the properties with default values as None
        self.data = data    # When I refer data as self.data it helps create a attribute "data" for a any "Node" object - Parameter is used to initialize the attribute
        self.next = next

    # Property/ parameter: head - The value is not passed as parameters to the __init__ function as the value is fixed, and the user does not decide the initial value 
    # If I would have passed head as a parameter, when a instance of class LinkedList is created, we need to pass the value for head 

# Methods: __init__, insert_at_beginning, 
class LinkedList:
    
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
        
    def print(self):
        # If the LL is empty
        if self.head is None:
            print("The LL is empty")
            return
        
        # If the LL is not empty
        itr = self.head 
        while itr:
            print(itr.data, end = "->")
            itr = itr.next
        print(None)

            
        
# Create a LL:
my_list = LinkedList()

# Add new nodes at the beginning
my_list.insert_at_beginning(2)
my_list.insert_at_beginning(3)
my_list.insert_at_beginning(4)

# Print the list
my_list.print()









# The Linked List itself will be an object of LinkedList class