# 1. reverse_inplace
# 2. is_palindrome



# Implement a Linked List in Python to store top 3 customers and their total sales amounts. 
# Your linked list should support:
#        1. Insertion of customer data (customer_id and total_amount).
#        2. Traversal to print all nodes.
#        3. Search for a specific customer_id.


class Node:
    def __init__(self, customer_id, total_sales):
        self.customer_id = customer_id
        self.total_sales = total_sales
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head = None
        

    def insert_data_at_end(self, customer_id, total_sales):
        new_node = Node(customer_id, total_sales)
        if self.head is None:
            self.head = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node
        
    def print_nodes(self):
        result = ""
        itr = self.head
        while itr:
            print(f"[Customer ID: {itr.customer_id}, Total Sales: {itr.total_sales}]", end=" -> ")
            itr = itr.next
        print(None)
        return result
    
    def search_customer_id(self, customer_id):
        itr = self.head
        while itr:
            if itr.customer_id == customer_id:
                return itr
            itr = itr.next
        return None
    
# Sample data:
customers = [
[101, 250.50],
[102, 300.75],
[103, 150.25],
[104, 500.00],
[105, 400.00]
]
# Get customer_id with top 3 total_sales
top_3_customers = sorted(customers, key=lambda x: x[1], reverse=True)[:3]

# Created a Linked List
my_list = linkedList()

# Insert customer_id with top 3 total_sales
for customer_id, total_sales in top_3_customers:
    my_list.insert_data_at_end(customer_id, total_sales)

# Print all the nodes    
my_list.print_nodes()

# Search with customer_id in the LL
my_list.search_customer_id(104)



    
    
            
