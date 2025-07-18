# Inheritance allows a child/derived class to reuse the properties and behaviors (methods, attributes) of another class (parent/base class)

# Example 1:

class Parent:                       # This is a Parent Class
    def greet(self):                # This is a instance method in Parent class 
        print("Hello from Parents")
        
class Child(Parent):                # Child class - because Parent class is passed to the Child class
    pass

c = Child()                         # Created a instance of Child class
c.greet()                           # Calling the method from Parent class using the instance of child class

# ?? How this works exactly??

# SUPER():
# If both parent and child define __init__(), the child's __init__ overrides the parent’s unless explicitly called using super()
# super() is used to access methods or constructors from the parent class

class Animal:                           # Parent Class
    def __init__(self, name):           # Constructor of Parent class
        self.name = name
        
    def speaks(self):
        print(f"{self.name} makes a sound")
        
class Dog(Animal):                      # Child Class
    def __init__(self, name, breed):    # Constructor of Child Class
        super().__init__(name)          # Call parent constructor - Instead of declaring self.name, we called Parent constructor 
        #self.name (from the Animal class) is set up correctly.
        #You don't have to duplicate the logic of the parent class
        # super() is used to access parent method 
        self.breed = breed
    
    def speaks(self):
        print(f"{self.name} barks")

d = Dog("Gracy", "Labrador")
d.speaks()


