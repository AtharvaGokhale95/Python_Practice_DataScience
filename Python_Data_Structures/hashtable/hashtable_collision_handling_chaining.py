# index = hash(key) % table_size
# What Python does when two different keys produce the same hash value

# Solution 1:
# Chaining: Append the key, values pair to the LL so that we can store values of multiple keys with same hash value at the same location in array


# Solution 1: Chaining Implementation:
# Initialize the arr with empty arrays instead of None as we need to store key, value pair when there is collision

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        # Now after determining the index, we want to handle collision. In self.arr, each element is a list.
        
        # Case 1: To check if the key already exists at idx h which now needs to be updated
        found = False
        for idx, element in enumerate(self.arr[h]):         # We are iterating inside the list at idx "h" in self.arr
            if element[0] == key:       # If the condition is satisfied, the same key we are trying to insert already exists and we need to just update its value
                self.arr[h][idx] = (key, value)     # As the key, value pair is stored as tuple, we cannot update them. We need to replace the tuple at that location
                found = True
                break
            
        # Case 1: Assume that the key does not already exist at idx "h"
        if found == False:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self, key):
        h = self.get_hash(key)
        # for element in self.arr[h]:
        #     if element[0] == key:
        #         element[1] = None
        # We cannot do this as the tuples are immutable and we cannot update the value to None
        
        for idx, element in enumerate(self.arr[h]):  # idx is required to point to the right key, value pair inside the list at idx "h"
            if element[0] == key:
                # self.arr[h][idx] = None
                del self.arr[h][idx]
                
        

if __name__ == "__main__":
    dict = HashTable()
    # march 6 and march 17 result into a collision
    dict['march 6'] = 120
    dict['march 6'] = 128
    dict['march 8'] = 132
    dict['march 8'] = 130
    dict['march 12'] = 133
    dict['march 17'] = 144
    print("The array looks like:", dict.arr)
    # print("The value on march 6 is :", dict['march 6'])
    # print("The value on march 8 is :", dict['march 8'])
    # print("The value on march 17 is :", dict['march 17'])
    del dict['march 12']
    print("The array now looks like:", dict.arr)
    

    