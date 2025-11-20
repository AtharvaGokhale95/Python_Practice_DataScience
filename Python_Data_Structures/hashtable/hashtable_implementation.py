# Hashtable implementation in Python is called Dictionaries
# key -> hash function -> int (idx of the allocated memory in RAM)
# value of that key is stores in the array a that particular index

# Hash Function: sum(ASCII) + Mode 

class HashTable:
    def __init__(self):
        self.MAX = 100                                  # Initialized the size of array to 100                          
        self.arr = [None for i in range(self.MAX)]      # Created an array of size 100 and initialized the value at each idx in the array to None
        # arr = [None, None, ........., None] - Array of 100 
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)       # ord(char) - return the ASCII value for each character of the key
        return h % self.MAX         # Mode operation: Sum of ASCII values for all chars in key % Size of array -> Number between 0 - (size of array - 1) -> Valid index
        # get_hash() return the valid index for a given char in key
        
    def add(self, key, value):      # Add a key, value pair to hash-table/ dictionary
        h = self.get_hash(key)      # returns the valid index of the array to store the value
        self.arr[h] = value
        # Here we can see that the array is indexed by keys and not values
        
    def __setitem__(self, key, value):      # python operator instead of add method
        h = self.get_hash(key)
        self.arr[h] = value
        
    
    def get(self, key):             # You can look-up in the dict only using a key
        h = self.get_hash(key)
        value = self.arr[h]         # returns the value at index = h in arr
        return value
    
    def __getitem__(self, key):     # python operator instead of get method
        h = self.get_hash(key)
        return self.arr[h]
        
if __name__ == "__main__":
    dict = HashTable()              # Each obj of class HashTable will have MAX and arr attributes
    dict.add('march 6', 130)
    dict.add('march 09', 135)
    dict.add('march 12', 138)
    dict.add('march 15', 139)
    dict['march 18'] = 140
    dict['march 21'] = 144
    # print("The array looks like:",dict.arr)
    print("The value on March 12 is:",dict.get('march 12'))
    print("The value on March 18 is:", dict['march 18'])