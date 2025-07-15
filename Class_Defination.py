# Class in an abstraction of a entity which has a common set of properties and methods
# Object of a Class: Object is a specific instance of a Class

class Person:
    def __init__(self, name):
        # self is the class itself - self refers to to current instance of the class
        # self gives access to instance variables and other methods defined in the class 
        # self is used to define properties of the class
        self.name = name
    # The __init__() method will be called every time we create a instance of this call
    # Even if we don't define the 
    
    def greet(self):
        print("Hello my name is", self.name)
        # Here using the self method we could access the variable from __init__ method - Accessing the instance variables
    
    def introduce(self):
        self.greet()  
        # Here we called another method defined in Person class using self

p = Person("Atharva")        # Now we have created an instance/ object of class Person - p is instance of class Person
# Thus, the __init__ method is called automatically when we create a instance of a class
p.introduce()

        
        