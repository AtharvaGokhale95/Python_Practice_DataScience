# Python_Programming
This is Github Repository for all the LeetCode Practice problems and the foundational logics of the basic Data Structures and Algorithms required for a Data Scientist role

Following are the key take-away from the solutions:

1. Two Sums
    1. To maintain 2 pointers, TC for list is O(n2) while for dict is O(n)
    2. When you run enumerate() on a list in Python, it returns an enumerate object that produces pairs of index and element as you loop over it
    3. In a standard Python dictionary, you can’t directly look up a key by its value, you can only lookup for the value using its key
    4. When we run "if val in dict" it always only looks of the keys if present in the dict and returns its value
    5. Whenever we lookup with a value in dict, we always pass a value of a key

2. Ways to call the function defined inside a class:
    1. Create a instance of a class and then call the method: object.method(parameters)
    2. Directly using the Class name: Class.method(object, parameters)
