# Python_Programming
This is Github Repository for all the LeetCode Practice problems and the foundational logics of the basic Data Structures and Algorithms required for a Data Scientist role

Video to create a venv: https://www.youtube.com/watch?v=bf7pCxj6mEg&t=254s&ab_channel=KrishNaik

Key points from the DSA perspectives:
1. Ways to call the function defined inside a class:
    1. Instance Method - Need to create a instance of a class and then call the method: object.method(parameters) - First arguement is self
    2. Class Method - Directly using the Class name: Class.method(object, parameters) - We can call a class method insider another class method
    3. Static Method - First arguement is the class itself - This method cannot refer to the object - Cannot access instance variable from class method

2. Definitions:
    1. Parameter - Variable in the function definition
    2. Arguement - The actual value passed to the function
    3. Attributes - Variables belonging to an object or class (Object Property) - Variable tied to a specific object 
    E.g.:
    ```python
    class CoffeeMachine:
    def __init__(self, coffee_type, sugar_level):  # parameters
        self.coffee_type = coffee_type             # attributes
        self.sugar_level = sugar_level

    def make_coffee(self):
        print(f"Making {self.coffee_type} with {self.sugar_level} sugar")

    # Calling the class with arguments
    machine = CoffeeMachine("Espresso", "1 teaspoon")  # arguments
    machine.make_coffee()  # Output: Making Espresso with 1 teaspoon sugar
    ```

3. Types of Inheritances:
    1. Single Inheritance
    ```python
        class Parent:
            pass
        class Child(Parent):
            pass
    ```

    2. Multiple Inheritance
    ```python
        class A:
            pass
        class B:
            pass
        class C(A, B):  # Inherits from both A and B
            pass
    ```
    
    3. Multilevel Inheritance
    ```python
        class A:
            pass
    class B(A):
        pass
    class C(B):
        pass
    ```

    4. Hierarchical Inheritance
    ```python
    class Parent:
        pass
    class Child1(Parent):
        pass
    class Child2(Parent):
        pass
    ```

4. Exception Handling in Python:

    1. Hierarchy of built-in exceptions:  
        BaseException
        ├── SystemExit
        ├── KeyboardInterrupt
        ├── GeneratorExit
        └── Exception
            ├── ArithmeticError
            ├── BufferError
            ├── LookupError
            ├── AssertionError
            ├── AttributeError
            ├── EOFError
            ├── FloatingPointError
            ├── GeneratorExit
            ├── ImportError
            ├── ModuleNotFoundError
            ├── IndexError
            ├── KeyError
            ├── KeyboardInterrupt
            ├── MemoryError
            ├── NameError
            ├── NotImplementedError
            ├── OSError
            ├── OverflowError
            ├── RecursionError
            ├── ReferenceError
            ├── RuntimeError
            ├── StopIteration
            ├── StopAsyncIteration
            ├── SyntaxError
            ├── IndentationError
            ├── TabError
            ├── SystemError
            ├── TypeError
            ├── UnboundLocalError
            ├── UnicodeError
            ├── ValueError
            └── ZeroDivisionError

    2. Definition of Exception class:
        ```python
        class Exception(BaseException):
            def __init__(self, *args):
                super().__init__(*args)
        ```
    
    3. Definition of BaseException class:
        ```python
        class BaseException:
            def __init__(self, *args):
                self.args = args

            def __str__(self):
                if len(self.args) == 1:
                    return str(self.args[0])
                return str(self.args)
        ```
         
    
    4. User defined exception:
        ```python
        class MyCustomError(Exception):
            def __init__(self, message):
                super().__init__(message)

        raise MyCustomError("Something went wrong!")
        ```

    5. Ways to Implement Exceptions:
        1. Built In Exceptions/ User Defined Exceptions:
            a. Single Except
            b. Multiple Except
        2. Using else and finally
        3. Raising Exceptions manually
  

Following are the key take-away from the solutions:

1. Two Sums
    1. To maintain 2 pointers, TC for list is O(n2) while for dict is O(n)
    2. When you run enumerate() on a list in Python, it returns an enumerate object that produces pairs of index and element as you loop over it
    3. In a standard Python dictionary, you can’t directly look up a key by its value, you can only lookup for the value using its key
    4. When we run "if val in dict" it always only looks of the keys if present in the dict and returns its value
    5. Whenever we lookup with a value in dict, we always pass a value of a key

2. isPalindrome:
    1. Using string/ list reversal: list = list[::-1]
    2. Using while loop: while head < tail, head = 0 and tail = len(str) - 1

3. Roman to Integer:
    1. When we want to keep a track of the current_value, previous_value and total_value, initialize previous_value and total_value == 0
    2. Update the previous_value with the value already looped on: previous_value = current_value
    3. Update the total_value based on the logic 

4. Longest Common Prefix:
    1. Sometimes we need to check for the complement condition instead of the actual condition in order to make the logic work:
        ```python
        a. if word[idx] == current_char:
                    prefix = prefix + current_char              # In this case we check if the new char is matching with current char in first word. But the problem is we are only able to check for the current word in strs list. We cannot check this condition for all the pending words before adding the char to prefix list
        b. if idx >= len(word) or word[idx] !=  current_char:
                    return prefix                               # By using this logic we take care of the idx going out of range
                                                                # And, if the word[idx] != current_char we can stop iterating there. This enables us to stop at the right place
5. Removed Duplicates:
    1. In-place: This means we update the original array by removing the duplicates from ith idx by replacing that idx with the next unique value
    2. For sorted array: We can maintain 2 indices, one to note the no of unique elements and other to read across the list
    3. For non-sorted array: We can initialize a set, and check every time if the value exits in the set, if not then update the value at that idx

6. Inplace update in an array:
    1. Updating a value inplace with a certain condition, means we re-write the whole array idx by idx
    2. So while updating we use a write_idx which will be updated based on the logic
    3. We the Inplace update can be done in a sequence, then we can use a write_idx and a read_idx where the read_idx will be iterated and the arr[write_idx] value will be updated
    4. If the inplace updated is not sequential, we need a separate data structure to implement the logic where we can store the idx visited to check every time

7. Occurence of a substring inside a string:
    1. How to validate continuous characters inside for loop: 
    ```python
    for i in range(0, len(haystack) - len(needle) + 1):     # Determining the range: Traverse only up to (len(haystack) - len(needle) + 1) as beyond this the complete substring cannot exist
            if haystack[i : i + len(needle)] == needle:     # This is the key logic: i : i + len(substring) - This validates continuous chars from the given idx
                return i
        return -1
    ```

8. 
    
        