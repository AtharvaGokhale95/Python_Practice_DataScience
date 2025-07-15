# Python_Programming
This is Github Repository for all the LeetCode Practice problems and the foundational logics of the basic Data Structures and Algorithms required for a Data Scientist role

Video to create a venv: https://www.youtube.com/watch?v=bf7pCxj6mEg&t=254s&ab_channel=KrishNaik

Key points from the DSA perspectives:
1. Ways to call the function defined inside a class:
    1. Create a instance of a class and then call the method: object.method(parameters)
    2. Directly using the Class name: Class.method(object, parameters)

2. Parameter - Variable in the function definition , Arguement - The actual value passed to the function




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
        a. if word[idx] == current_char:
                    prefix = prefix + current_char              # In this case we check if the new char is matching with current char in first word. But the problem is we are only able to check for the current word in strs list. We cannot check this condition for all the pending words before adding the char to prefix list
        b. if idx >= len(word) or word[idx] !=  current_char:
                    return prefix                               # By using this logic we take care of the idx going out of range
                                                                # And, if the word[idx] != current_char we can stop iterating there. This enables us to stop at the right place                       